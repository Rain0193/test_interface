# -*- coding:utf-8 -*-
'''
Created on 2017年6月1日

@author: lt
'''
import Testdata
#初始化测试数据
def init():
    #删除上次测试的数据
    Testdata.common()
    Testdata.account_del()#删除accountDocument测试数据
    Testdata.course_del()#删除courseDocument测试数据
    Testdata.item_del()#删除courseItemDocument测试数据
    Testdata.forum_del()#删除forumDocument测试数据
    Testdata.version_del()#删除versionDocument测试数据
    Testdata.ad_del()#删除adDocument测试数据
    Testdata.region_del()#删除regionDocument测试数据
    Testdata.templet_del()#删除temletDocument测试数据
    Testdata.adminaccount_del()#删除adminaccountDocument测试数据
    Testdata.creditCode_del()#删除creditCodeDocument测试数据
    Testdata.requestRecode_del()#删除requestRecordDocument测试数据
    Testdata.roleId_del()#删除roleDocumentc测试数据
    Testdata.PlayRecord_del()#删除playRecordDocument测试数据
    #构造测试数据
    Testdata.account()#初始化accountDocument测试数据
    Testdata.course()#初始化courseDocument测试数据
    Testdata.item()#初始化courseItemDocument测试数据
    Testdata.forum()#初始化forumDocument测试数据
    Testdata.version()#初始化versionDocument测试数据
    Testdata.ad()#初始化adDocument测试数据
    Testdata.region()#初始化regionDocument测试数据
    Testdata.templet()#初始化temletDocument测试数据
    Testdata.adminaccount()#初始化adminaccountDocument测试数据
    Testdata.creditCode()#初始化creditCodeDocument测试数据
    Testdata.requestRecode()#初始化requestRecordDocument测试数据
    Testdata.roleId()#初始化roleDocumentc测试数据
    Testdata.PlayRecord()#初始化playRecordDocument测试数据