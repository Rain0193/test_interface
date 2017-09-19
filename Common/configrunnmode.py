# -*- coding:utf-8 -*-
'''
Created on 2017年5月5日

@author: lt
'''
import configparser
import Path
from Exception import Custom_exception
class ConfigRunMode:
    #读取运行模式和运行用例表
    #runmode  0运行部分用例，1运行全部用例
    #sheet 0运行前端接口，1运行后端接口
    def __init__(self ):
        config = configparser.ConfigParser()
        config.read(Path.run_case_config_Path())
        try:
            self.run_mode = config['RUNCASECONFIG']['runmode']
            self.run_mode = int(self.run_mode)
            self.front_case_list = config['RUNCASECONFIG']['front_case_id']
            self.front_case_list = eval(self.front_case_list) 
            self.background_case_list = config['RUNCASECONFIG']['background_case_id']
            self.background_case_list = eval(self.background_case_list)
            self.sheet = config['RUNCASECONFIG']['sheet']
            self.sheet = int(self.sheet)
        except Exception as e:
            print('%s', e)
            raise Custom_exception.read_config
    def get_run_mode(self):
        return self.run_mode
    def get_case_list(self):
        if self.sheet==0:
            return  self.front_case_list
        elif self.sheet==1:
            return self.background_case_list
    def get_sheet(self):
        return self.sheet