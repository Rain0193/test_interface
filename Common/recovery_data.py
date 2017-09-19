# -*- coding:utf-8 -*-
'''
Created on 2017年6月1日

@author: lt
'''
from initialized import Testdata
def Recovery_data():
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