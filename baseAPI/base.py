import requests
import yaml
import json

'''封装请求接口的函数，适合于需要校验登录权限的接口，
设置_headers为了减少再参数化用例的时候减少headers: xxx的步骤
加上**kwargs的参数为了请求接口便于传入其他参数，例如cookies= xx, files= xx
'''
def send(body, headers=None, **kwargs):
    if headers is None:
        _headers = {
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Type": "application/json"
        }
        return requests.request(**body, headers=_headers, **kwargs)
    else:
        return requests.request(**body, headers=headers, **kwargs)
