import json
import requests
import pytest
import time
# d='{"admin":"123"}'
# print(type(d))
# d1=eval(d)
# print(d1)
# print(type(d1))

# def fuc_y(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# c=range(1,5)
# d={'a':1,'b':2,'c':'sss'}
# fuc_y(*c,**d)

# @pytest.mark.skip('阻塞，跳过')
# @pytest.mark.parametrize('shuru,shuchu', [('3+5', 8), ('4+6', 10), ('5+7', 12)])
# def test_demo(shuru, shuchu):
#     assert eval(shuru) == shuchu

class Father():
    def __fangzi(self):
        print('父亲的房子')
class People(Father):
    def __init__(self):
        self.age=18
        self.name='xiaofang'
    def __kandianying(self):
        print('看电影')
        return '我就看电影'

    def dayouxi(self):
        a=self.__kandianying()
        print(a)
        print('打游戏')

nv=People()
print(nv.age)
nv.dayouxi()

