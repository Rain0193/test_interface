# -*- coding:utf-8 -*-
'''
Created on 2017年5月5日

@author: lt
'''
import requests
# 配置类
class ConfigHttp:
    '''配置要测试接口服务器的ip、端口、域名等信息，封装http请求方法，http头设置'''

    def __init__(self):
        pass
    # 封装HTTP GET请求方法
    def get(self,url, params,host):
        #headers = {'Content-type':'application/json'}
        params = eval(params)
        url = 'http://' + host + url 
        try:
            response = requests.get(url,params=params)
            return response.json(),response.status_code
        except Exception as e:
            print'%s' % e
            return {},response.status_code
        # 封装HTTP POST请求方法
    def post(self, url, data, host,files=None):
        #headers = {'Content-type':'application/json'}
        data = eval(data)
        try:
            url = 'http://' + host   + url 
            response= requests.post(url, data=data,files=files)       
            return response.json(),response.status_code
        except Exception as e:
            print '%s' %e
            return {},response.status_code