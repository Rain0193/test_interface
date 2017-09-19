# -*- coding:utf-8 -*-
'''
Created on 2017年5月5日

@author: lt
'''
import configparser
import Common.Path
class Configemail:
    #读取邮件发送配置信息
    def __init__(self ):
        config = configparser.ConfigParser()
        config.read(Common.Path.email_Path())
        try:
            self.Sender = config['email_address']['Sender']#发件人地址
            self.Addressee = config['email_address']['Addressee']#收件人地址，多个收件人用逗号隔开
            self.smtp = config['email_address']['smtp']#第三方smtp，例如网易的，smtp.163.com
            self.login = config['email_address']['login']#授权登录账号
            self.AuthorizationCode = config['email_address']['AuthorizationCode']#授权码
        except Exception as e:
            print('%s', e)
    def get_Sender(self):
        return self.Sender
    def get_Addressee(self):
        return  self.Addressee
    def get_smtp(self):
        return  self.smtp
    def get_login(self):
        return  self.login
    def get_AuthorizationCode(self):
        return  self.AuthorizationCode

