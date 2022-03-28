import time
import urllib3
import allure
from common.read_config import config

urllib3.disable_warnings()

#从配置文件获取Host
baseurl = '/conf/product_center/env.ini'
config = config(baseurl)
Host = config['Host']['Host']
# 获取当前时间戳：10位 字符串
nowTime = str(int(time.time()))

@allure.feature("获取用户信息模块")
class TestUserinfo:
    @allure.story("获取用户信息成功")
    @allure.title('正确token，获取用户信息成功')
    def test_userinfo(self,login_fix):
        '''正确的token获取用户信息'''
        s = login_fix
        url = Host + '/api/product/center/user/getUserInfo'
        parms = '_t=' + nowTime + ''
        r = s.get(url, json=parms)
        print({'response': r.json()})
        assert r.json()['code'] == 1001

    @allure.story("获取用户信息失败")
    @allure.title('错误token，获取用户信息失败')
    def test_userinfoerror(self,unlogin_fix):
        '''无效token无法获取用户信息'''
        s = unlogin_fix
        url = Host + '/api/product/center/user/getUserInfo'
        parms = '_t=' + nowTime + ''
        r = s.get(url, json=parms, verify=False)
        print({'response': r.json()})
        assert r.json()['code'] == 500
        assert r.json()['msg'] == 'token无效'
