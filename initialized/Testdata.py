# -*- coding:utf-8 -*-
'''
Created on 2017年6月1日

@author: lt
'''
from Common import ReadExcel
from Common import Path
from Common import getdb
from bson.objectid import ObjectId
read=ReadExcel.Excel(Path.case_Path())
db=getdb.mongodb()
def common():
    db.db_update('accountDocument', {'mobile':'18202886909'}, {'mobile':'18202886913'})
    db.db_drop('accountDocument', {'mobile':'18202886910'})#删除用于注册的用户数据
def account():
    read.excel_table_byname(u'用户初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_insert('accountDocument', eval(read.get_init(i)))
def account_del():
    read.excel_table_byname(u'用户初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('accountDocument', {"_id":ObjectId("%s" %read.get_del(i))})
def course():
    read.excel_table_byname(u'课程初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_insert('courseDocument', eval(read.get_init(i)))
def course_del():
    read.excel_table_byname(u'课程初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('courseDocument', {"_id":ObjectId("%s" %read.get_del(i))})
def item():
    read.excel_table_byname(u'课时初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_insert('courseItemDocument', eval(read.get_init(i)))    
def item_del():
    read.excel_table_byname(u'课时初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('courseItemDocument', {"_id":ObjectId("%s" %read.get_del(i))})
def forum():
    read.excel_table_byname(u'讲堂初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):   
        db.db_insert('forumDocument', eval(read.get_init(i)))
def forum_del():
    read.excel_table_byname(u'讲堂初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('forumDocument', {"_id":ObjectId("%s" %read.get_del(i))}) 
def version():
    read.excel_table_byname(u'版本号初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):      
        db.db_insert('versionDocument', eval(read.get_init(i)))
def version_del():
    read.excel_table_byname(u'版本号初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('versionDocument', {"_id":ObjectId("%s" %read.get_del(i))})  
def ad():
    read.excel_table_byname(u'广告初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):       
        db.db_insert('adDocument', eval(read.get_init(i)))
def ad_del():
    read.excel_table_byname(u'广告初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('adDocument', {"_id":ObjectId("%s" %read.get_del(i))})   
def region():
    read.excel_table_byname(u'地域初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):      
        db.db_insert('regionDocument', eval(read.get_init(i)))
def region_del():
    read.excel_table_byname(u'地域初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('regionDocument', {"_id":ObjectId("%s" %read.get_del(i))}) 
def templet():
    read.excel_table_byname(u'静态网页初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):        
        db.db_insert('templetDocument', eval(read.get_init(i)))
def templet_del():
    read.excel_table_byname(u'静态网页初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('templetDocument', {"_id":ObjectId("%s" %read.get_del(i))}) 
def adminaccount():
    #构造后台用户测试数据
    read.excel_table_byname(u'后台用户初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):        
        db.db_insert('adminAccountDocument', eval(read.get_init(i)))
def adminaccount_del():
    read.excel_table_byname(u'后台用户初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('adminAccountDocument', {"_id":ObjectId("%s" %read.get_del(i))}) 
def creditCode():
    #构造授信码查询数据
    read.excel_table_byname(u'授信码初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):        
        db.db_insert('creditCodeDocument', eval(read.get_init(i)))
def creditCode_del():
    #删除授信码初始化数据
    read.excel_table_byname(u'授信码初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('creditCodeDocument', {"_id":ObjectId("%s" %read.get_del(i))}) 
def requestRecode():
    #构造接口请求查询数据
    read.excel_table_byname(u'接口请求初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):        
        db.db_insert('requestRecordDocument', eval(read.get_init(i)))
def requestRecode_del():
    #删除接口请求初始化数据
    read.excel_table_byname(u'接口请求初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('requestRecordDocument', {"_id":ObjectId("%s" %read.get_del(i))}) 
def roleId():
    #构造角色初始化数据
    read.excel_table_byname(u'角色初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):        
        db.db_insert('roleDocument', eval(read.get_init(i)))
def roleId_del():
    #删除角色初始化数据
    read.excel_table_byname(u'角色初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('roleDocument', {"_id":ObjectId("%s" %read.get_del(i))})
def PlayRecord():
    #构造播放记录初始化测试数据
    read.excel_table_byname(u'播放记录初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_insert('playRecordDocument', eval(read.get_init(i)))
def PlayRecord_del():
    #删除播放记录初始化测试数据
    read.excel_table_byname(u'播放记录初始化测试数据')
    num=read.get_nrows()
    for i in range(1,num):
        db.db_drop('playRecordDocument', {"_id":ObjectId("%s" %read.get_del(i))})
