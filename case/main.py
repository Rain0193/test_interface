# -*- coding:utf-8 -*-
'''
Created on 2017年5月5日

@author: lt
'''
from testreport.Report import report
from runcase import Runcase
from Common.globalconfig import Global
from testreport.Send_report import send_email
from initialized import initialized_data
from Common import recovery_data
from initialized import create_case
if __name__ == '__main__':
    #初始化测试数据
    #initialized_data.init()
    #初始化测试用例脚本
    create_case.edit_case()
    # 全局配置
    '''global_config = Global()
    test_report=report()
    fp=test_report.get_fp()
    test_time=test_report.get_time()#测试开始时间
    run_mode = global_config.get_run_mode() # 运行模式
    run_case_list = global_config.get_run_case_list()  # 需要运行的用例列表
    http = global_config.get_http()           # http
    #初始化测试报告
    runner = test_report.build_report()
    #运行测试用例
    case_runner = Runcase()
    case_runner.runcase(runner, run_mode, run_case_list, http)
    #测试报告生成后，释放资源
    fp.close()
    #测试完成，恢复数据
    recovery_data.Recovery_data()
    #发送测试报告
    #send_email(test_time)'''
