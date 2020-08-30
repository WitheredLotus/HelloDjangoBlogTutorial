# -*- coding = utf-8 -*-
# @Time : 2020/7/12 20:38
# @Author : EmperorHons
# @File : production.py
# @Software : PyCharm
from .common import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['hellodjangoblogtutorial.tiangaodijiong.com']