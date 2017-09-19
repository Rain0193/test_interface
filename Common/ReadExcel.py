# -*- coding:utf-8 -*-
'''
Created on 2017年5月5日

@author: lt
'''
#读取测试用例
import xlrd
class Excel:

    def __init__(self,fp):
        try:
            self.data=xlrd.open_workbook(fp)
        except Exception,e:
            print str(e)
    #通过名称索引读取表格数据
    def excel_table_byname(self,sheet_name):
        try:
            self.table=self.data.sheet_by_name(sheet_name)
            self.nrows=self.table.nrows  #行数
        except:
            print '读取测试用例失败'
    def get_nrows(self):
        return self.nrows           #测试用例数量
    def get_case_desc(self,case_id):
        return self.table.row(case_id)[2].value #测试用例描述
    def get_http(self,case_id):
        return self.table.row(case_id)[3].value #http方式
    def get_test_mode(self,case_id):
        return self.table.row(case_id)[4].value  #测试方法
    def get_host(self,case_id):
        return self.table.row(case_id)[5].value  #测试域名
    def get_url(self,case_id):
        return self.table.row(case_id)[6].value  #接口地址
    def get_data(self,case_id):
        return self.table.row(case_id)[7].value  #传递参数
    def get_file(self,case_id):
        return self.table.row(case_id)[8].value #是否上传图片
    def get_expect_code(self,case_id):
        return self.table.row(case_id)[9].value  #code
    def get_expect_data(self,case_id):
        return self.table.row(case_id)[10].value  #期望返回的data数据
    def get_expect_msg(self,case_id):
        return self.table.row(case_id)[11].value  #期望返回的msg
    def get_expect_http(self,case_id):
        return self.table.row(case_id)[12].value    #期望返回的http
    def get_del_add(self,case_id):
        return self.table.row(case_id)[16].value #删除测试中新增的数据
    def get_init(self,num):
        return self.table.row(num)[1].value #测试初始化数据
    def get_del(self,num):
        return self.table.row(num)[2].value #删除测试数据


