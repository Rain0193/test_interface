# -*- coding:utf-8 -*-
'''
Created on 2017年5月5日

@author: lt
'''
#封装配置文件地址
from globalconfig import Global
#运行模式文件路径
def run_case_config_Path():
    path='E:\\project\\test_interface\\run_case_config.ini'
    return path
#测试用例文件路径
def case_Path():
    path='E:\\project\\test_interface\\case.xls'
    return path
#测试类
def sheet_name_Path():
    global_config = Global()
    sheet=global_config.get_sheet()
    if sheet==0:      
        path=u'前端接口'
        return path
    elif sheet==1:
        path=u'后台接口'
        return path
#测试报告生成路径
def report_Path():
    path='E:\\project\\test_interface\\Report\\'
    return path
#发送测试报告邮箱配置
def email_Path():
    path='E:\\project\\test_interface\\email_address.ini'
    return path
#写入Excel位置
def sheet_number_Path():
    global_config = Global()
    sheet=global_config.get_sheet()
    return sheet
#mongo数据库配置
def get_db():
    path='E:\\project\\test_interface\\db_config.ini'
    return path
#上传图片位置
def photo_Path():
    path='E:\\project\\test_interface\\cover.jpg'
    return path