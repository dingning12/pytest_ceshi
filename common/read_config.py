# encoding=utf-8
from configparser import ConfigParser as conf
import os

current_dir = os.path.dirname(os.path.dirname(__file__))

#封装这个函数是为了读取配置文件的数据
def config(path):
    config = conf()
    absolute_path = current_dir + path
    config.read(absolute_path)
    return config


if __name__ == '__main__':
    common_config_path = '/conf/product_center/env.ini'
    config = config(common_config_path)
    Host = config['Host']['Host']
    port = int(config['DB']['PORT'])
    print(port)
    print(type(port))
    print(config.sections())
    print(config.options('DB'))
    print(Host)
    print(type(Host))
