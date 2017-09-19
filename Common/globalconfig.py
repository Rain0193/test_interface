# -*- coding:utf-8 -*-
'''
Created on 2017年5月5日

@author: lt
'''
from confighttp import ConfigHttp

from configrunnmode import ConfigRunMode
class Global:
    def __init__(self):
        self.http = ConfigHttp()
        self.run_mode_config = ConfigRunMode()
    def get_http(self):
        return self.http
    def get_run_mode(self):
        return self.run_mode_config.get_run_mode()
    def get_run_case_list(self):
        return self.run_mode_config.get_case_list()
    def get_sheet(self):
        return self.run_mode_config.get_sheet()
