class Config:
    """多套环境的公共配置"""
    version = "v1.0"
    # 钉钉群机器人通知
    # DING_TALK = {
    #     "access_token": "****复制你的token****",
    # }


class TestConfig(Config):
    """测试环境"""
    BASE_URL = 'http://httpbin.org'
    BASE_URL2 = 'http://www.example.com'
    USERNAME = "test"


class UatConfig(Config):
    """联调环境"""
    BASE_URL = 'http://www.baidu.com'


# 环境关系映射
env = {
    "test": TestConfig,
    "uat": UatConfig
}
