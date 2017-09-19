# -*- coding:utf-8 -*-
'''
Created on 2017年5月5日

@author: lt
'''
#自定义异常类，可自行添加
class Request_fail(Exception):  
    def __init__(self,err='返回http状态错误'):  
        Exception.__init__(self,err)
class assert_error(Exception):  
    def __init__(self,err='断言错误'):  
        Exception.__init__(self,err)
class Database_connection_failed(Exception):
    def __init__(self,err='连接数据库失败'):
        Exception.__init__(self,err)
class Content_is_null(Exception):
    def __init__(self,err='数据库搜索内容结果为空'):
        Exception.__init__(self,err)
class update_database(Exception):
    def __init__(self,err='更新数据库内容失败'):
        Exception.__init__(self,err)
class del_database(Exception):
    def __init__(self,err='删除数据库内容失败'):
        Exception.__init__(self,err)
class read_config(Exception):
    def __init__(self,err='读取配置文件失败'):
        Exception.__init__(self,err)
class add_data(Exception):
    def __init__(self,err='测试数据初始化失败'):
        Exception.__init__(self,err)
class data_err(Exception):
    def __init__(self,err='返回的data数据错误'):
        Exception.__init__(self,err)
class data_err2(Exception):
    def __init__(self,err='返回data内容缺失，或键值为空'):
        Exception.__init__(self,err)
class del_test_data(Exception):
    def __init__(self,err='删除新增接口产生的测试数据失败'):
        Exception.__init__(self,err)
class NO_json(Exception):
    def __init__(self,err='返回http状态200，但无json数据返回'):
        Exception.__init__(self,err)


