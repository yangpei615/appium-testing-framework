import configparser
import os

# 获取项目根目录
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# 配置文件路径
CONFIG_FILE = os.path.join(ROOT_DIR, '..', 'config.ini')

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(CONFIG_FILE, encoding='utf-8')

    def get_login(self, key):
        return self.config.get('login', key)

    def get_app(self, key):
        return self.config.get('app', key)

# 全局实例
conf = Config()