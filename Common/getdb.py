# -*- coding:utf-8 -*-
'''
Created on 2017年6月1日

@author: lt
'''
import pymongo
import configparser
import Path
from Exception import Custom_exception
#连接mongo数据库
class mongodb:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(Path.get_db())
        try:
            self.host = config['MongoDB']['host']
            self.port = config['MongoDB']['port']
            self.port = int(self.port)
            self.user = config['MongoDB']['user']
            self.pwd = config['MongoDB']['pwd']
            self.datebase = config['MongoDB']['db']
        except Exception as e:
            print '%s' %e
            raise Custom_exception.read_config
        try:         
            self.client = pymongo.MongoClient(self.host,self.port)
            self.db =self.client.mamainstdb
            self.db.authenticate("mamainstdbuser", "mamainstdbpassword")
        except Exception as e:
            print '%s' %e
            raise Custom_exception.Database_connection_failed
    def db_find(self,collection,where):
        #查询文档
        try:
            collection = self.db[collection]
            self.list=list(collection.find(where))
            if self.list == {}:
                raise Custom_exception.Content_is_null
            return self.list
        except Exception as e:
            print '%s' %e
            raise        
    def db_update(self,collection,where,update):
        #修改文档
        try:
            collection = self.db[collection]
            collection.update(where,{'$set':update})
        except Exception as e:
            print '%s' %e
            raise Custom_exception.update_database
    def db_drop(self,collection,where):
        #删除文档
        try:
            collection = self.db[collection]
            collection.remove(where)
        except Exception as e:
            print '%s' %e
            raise Custom_exception.del_database
    def db_replace(self,collection,where,update):
        try:
            collection = self.db[collection]
            collection.update(where,update)
        except Exception as e:
            print '%s' %e
            raise Custom_exception.update_database
    def db_insert(self,collection,where):
        try:
            collection=self.db[collection]
            collection.insert(where)
        except Exception as e:
            print '%s' %e
            raise Custom_exception.add_data