import pytest
import requests
# from case.common_case import login
from  case.common_case import Productcenter


@pytest.fixture(scope='module')# module:每个py文件调用一次  session：只调用一次 #function py文件中每条用例都执行
def login_fix():
    ''' 自定义一个前置操作 '''
    print('先登录')
    s = requests.session()
    shili=Productcenter(s)
    shili.login()

    return s




@pytest.fixture(scope='function')
def unlogin_fix():
    '''自定义一个前置操作'''
    print('不登录')
    s = requests.session()
    h = {'Authorization': 'a4b306fa1-0575-450c-9dd8-4cbb9cb0333f'}
    s.headers.update(h)
    return s

if __name__ == '__main__':
    print(login_fix())
