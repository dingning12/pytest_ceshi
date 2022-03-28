import requests
import time
from common.read_config import config

#从配置文件获取host
baseurl = '/conf/product_center/env.ini'
conf=config(baseurl)
Host = conf['Host']['Host']
# 获取当前时间戳：10位 字符串
nowTime = str(int(time.time()))


class Productcenter():
    def __init__(self, s):
        self.s = s  #s传 requests.session()

    def login(self):
        url = Host + '/api/product/center/user/login'
        parms = 'username=admin&password=123456&_t=' + nowTime + ''
        r = self.s.get(url, params=parms, verify=False)
        # print(r.content)#byte类型，解决乱码这么用 r.contend.decode("utf-8"),转为str类型
        # r.content.decode("utf-8") 转为str类型
        # print(r.text)# str类型
        try:
            token = r.json()['data']['token']  # 获取token
            h = {'Authorization': '%s' % token}
            self.s.headers.update(h)  # 把token更新到headers
            print({'response_login': r.json()})  # dict类型，返回响应
        except TypeError:
            print({'登录失败':r.json()['code']})


        #print({'header': s.headers})


if __name__ == '__main__':
    s = requests.session()  # 会话
    # login(s)
    shili=Productcenter(s)
    shili.login()
