# -*- coding = utf-8 -*-
# @Time : 2020/6/21 13:32
# @Author : EmperorHons
# @File : fake.py
# @Software : PyCharm

import os
import pathlib
import random
import sys
from datetime import timedelta
import django
import faker
from django.utils import timezone


# 将项目根目录添加到 Python 的模块搜索路径中
back = os.path.dirname
BASE_DIR = back(back(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjangoblogtutorial.settings.local")
    django.setup()

    from blog.models import Category, Post, Tag
    from comments.models import Comment
    from django.contrib.auth.models import User

    print('clean database')
    Post.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()
    Comment.objects.all().delete()
    User.objects.all().delete()

    print('create a blog user')
    user = User.objects.create_superuser('admin', 'admin@hellogithub.com', 'admin')
    category_list= ['Python学习笔记', '开源项目', '工具资源', '程序员生活感悟', 'test category']
    tag_list = ['django', 'Python', 'Pipenv', 'Docker', 'Dockerfile', 'Elasticsearch', 'Gunicorn', 'supervisor', 'test tag']
    a_year_ago = timezone.now() - timedelta(days=365)

    print('create categories and tags')
    for cate in category_list:
        Category.objects.create(name=cate)

    for tag in tag_list:
        Tag.objects.create(name=tag)

    print('create a markdown sample post')
    Post.objects.create(
        title='Markdown 与代码高亮测试',
        body=pathlib.Path(BASE_DIR).joinpath('scripts', 'md.sample').read_text(encoding='utf-8'),
        category=Category.objects.create(name='Markdown测试'),
        author=user,
    )

    print('create some faked posts published within the post year')
    fake = faker.Faker('zh_CN')  # 实例化一个 Faker 对象 生成数据，Faker 默认生成英文数据
    for _ in range(100):
        tags = Tag.objects.order_by('?')
        tag1 = tags.first()
        tag2 = tags.last()
        cate = Category.objects.order_by('?').first()  # order_by('?')返回随机排序的结果，随机选择标签(Tag) 和分类(Category)
        created_time = fake.date_time_between(start_date='-1y', end_date="now", tzinfo=timezone.get_current_timezone())
        # fake.date_time_between 返回 2 个指定日期间的随机日期，三个参数分别是起始日期，终止日期和时区。 -1y 为 1年前
        post = Post.objects.create(
            title=fake.sentence().rstrip('.'),
            body='\n\n'.join(fake.paragraphs(10)),
            # fake.paragraphs(10) 用于生成 10 个段落文本，以列表形式返回，列表的每个元素即为一个段落
            # 2 个换行符连起来是为了符合 Markdown 语法，Markdown 中只有 2 个换行符分隔的文本才会被解析为段落。
            created_time=created_time,
            category=cate,
            author=user,
        )
        post.tags.add(tag1, tag2)
        post.save()

    print('create some comments')
    for post in Post.objects.all()[:20]:
        post_created_time = post.created_time
        delta_in_days = '-' + str((timezone.now() - post_created_time).days) + 'd'
        # 评论的发布时间必须位于被评论文章的发布时间和当前时间之间
        for _ in range(random.randrange(3, 15)):
            Comment.objects.create(
                name=fake.name(),
                email=fake.email(),
                url=fake.uri(),
                text=fake.paragraph(),
                created_time=fake.date_time_between(
                    start_date=delta_in_days,
                    end_date="now",
                    tzinfo=timezone.get_current_timezone()),
                post=post,
            )
    print('done!')
