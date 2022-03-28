import requests
import time
import pytest
import allure
from common.read_yml import readyml
from common.read_config import config


#从配置文件获取Host
baseurl = '/conf/product_center/env.ini'
config = config(baseurl)
Host = config['Host']['Host']

# 获取当前时间戳：10位 字符串
nowTime = str(int(time.time()))
s = requests.session()  # 会话

testdata=readyml('/testdata/login_data.yml')['logindata'] #读取这个路径下yml文件里的数据

# testdata = [('admin', '123456', {'code': 1001, 'message': '请求成功'}),
#             ('admin1', '123456', {'code': 801, 'message': '用户名或者密码错误'}),
#             ('admin', '1234567', {'code': 801, 'message': '用户名或者密码错误'})]

@allure.feature("登录模块")
@pytest.mark.parametrize('username,password,expect',
                         testdata,
                         ids=['账号密码正确，登录成功', '账号错误，登录失败', '密码错误，登录失败'])
def test_login(username, password, expect):
    url = Host + '/api/product/center/user/login'
    parms = 'username=' + username + '&password=' + password + '&_t=' + nowTime + ''
    r = s.get(url, params=parms, verify=False)
    print(r.json())  # dict类型
    assert r.json()['code'] == expect['code']
    assert r.json()['message'] == expect['message']


# def test_normallogin(username='admin', password='123456'):
#     url = baseurl + '/api/product/center/user/login'
#     parms = 'username=' + username + '&password=' + password + '&_t=' + nowTime + ''
#     r = s.get(url, params=parms, verify=False)
#     print(r.json())  # dict类型
#     assert r.json()['code'] == 1001
#
#
#
# def test_accounterror():
#     url = baseurl + '/api/product/center/user/login'
#     parms = 'username=admin1&password=123456&_t=' + nowTime + ''
#     r = s.get(url, params=parms, verify=False)
#     print(r.json())
#     assert r.json()['code'] == 801
#     assert r.json()['message'] == '用户名或者密码错误'
#
#
# def test_passworderror():
#     url = baseurl + '/api/product/center/user/login'
#     parms = 'username=admin&password=1234567&_t=' + nowTime + ''
#     r = s.get(url, params=parms, verify=False)
#     print(r.json())
#     assert r.json()['code'] == 801
#     assert r.json()['message'] == '用户名或者密码错误'



