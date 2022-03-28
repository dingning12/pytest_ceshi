import yaml
import os

path = os.path.dirname(os.path.dirname(__file__))


def readyml(ymlpath):
    ''' 读取yml文件内容'''
    ymlpath = path + ymlpath
    if not os.path.isfile(ymlpath):
        raise FileNotFoundError('文件路径不存在，请检查路径是否正确')
    with open(ymlpath, 'r', encoding='utf-8') as f:
        cfg = f.read()
        d = yaml.load(cfg,Loader=yaml.FullLoader)
        print('读取的文件数据：%s' % d)
        return d


if __name__ == '__main__':
    print(readyml('/common/login_data.yml')['logindata'])
    print(os.path.dirname(os.path.realpath(__file__)))
    print(path)
