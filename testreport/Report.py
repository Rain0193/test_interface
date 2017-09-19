# -*- coding:utf-8 -*-
'''
Created on 2017年5月5日

@author: lt
'''
import time
import HTMLTestRunner
import Common.Path
#测试报告初始化
class report:
    def __init__(self):
        self.time=time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
        self.file=Common.Path.report_Path()+self.time+".html"
        self.fp = file(self.file,'wb')
    def build_report(self):
        runner = HTMLTestRunner.HTMLTestRunner(stream=self.fp,title='test_report',description='mamainst_test_interface')
        return runner
    def get_time(self):
        return self.time
    def get_fp(self):
        return self.fp