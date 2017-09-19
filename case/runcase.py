# -*- coding:utf-8 -*-
'''
Created on 2017年5月5日

@author: lt
'''
import unittest
from test_interface_case import TestInterfaceCase
from Common import ReadExcel
import Common.Path

class Runcase:
    def __init__(self):
        pass

    def runcase(self , runner , run_mode , run_case_list ,http):
        case=ReadExcel.Excel(Common.Path.case_Path())
        case.excel_table_byname(Common.Path.sheet_name_Path())
        Num=case.get_nrows()
        suite=unittest.TestSuite()
        #运行全部测试用例
        if run_mode==1:
            for case_id in range(1,Num):
                test_method = case.get_test_mode(case_id)
                host=case.get_host(case_id)
                request_url = case.get_url(case_id)
                request_param = case.get_data(case_id)
                code=case.get_code(case_id).encode('utf-8')
                case_desc=case.get_case_desc(case_id).encode('utf-8')
                expect_http=case.get_expect_http(case_id)
                test=TestInterfaceCase(test_method,request_url,http,request_param,host,case_id,code,case_desc,expect_http)
                suite.addTest(test)
            runner.run(suite) 
        #运行部分测试用例
        else:
            for case_id in run_case_list:
                test_method = case.get_test_mode(case_id)
                host=case.get_host(case_id)
                request_url = case.get_url(case_id)
                request_param = case.get_data(case_id)
                code=case.get_code(case_id).encode('utf-8')
                case_desc=case.get_case_desc(case_id).encode('utf-8')
                expect_http=case.get_expect_http(case_id)
                test=TestInterfaceCase(test_method,request_url,http,request_param,host,case_id,code,case_desc,expect_http)
                suite.addTest(test)
            runner.run(suite) 
            
        