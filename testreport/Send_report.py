#-*- coding: utf-8 -*-  
import smtplib  
import email.MIMEMultipart# import MIMEMultipart  
import email.MIMEText# import MIMEText  
import os.path  
import mimetypes  
import email.MIMEImage# import MIMEImage  
import configemail
from Common.Path import report_Path
def send_email(test_time):
    address=configemail.Configemail()
    From = address.get_Sender()#发件人地址
    To = address.get_Addressee()#收件人地址，多个收件人用逗号隔开
    file_name = report_Path()+test_time+'.html'#附件名  
    
    server = smtplib.SMTP(address.get_smtp())  
    server.login(address.get_login(),address.get_AuthorizationCode()) #仅smtp服务器需要验证时   
  
    # 构造MIMEMultipart对象做为根容器 
    main_msg = email.MIMEMultipart.MIMEMultipart()  
  
    # 构造MIMEText对象做为邮件显示内容并附加到根容器  
    text_msg = email.MIMEText.MIMEText("妈妈学院接口测试报告",_charset="utf-8")  
    main_msg.attach(text_msg)  
  
    # 构造MIMEBase对象做为文件附件内容并附加到根容器 
    ctype,encoding = mimetypes.guess_type(file_name)  
    if ctype is None or encoding is not None:  
        ctype='application/octet-stream'  
    maintype,subtype = ctype.split('/',1)  
    file_msg=email.MIMEImage.MIMEImage(open(file_name,'rb').read(),subtype)  
    print ctype,encoding  
    ## 设置附件头 
    basename = os.path.basename(file_name)  
    file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头  
    main_msg.attach(file_msg)  
  
    # 设置根容器属性  
    main_msg['From'] = From  
    main_msg['To'] = To  
    main_msg['Subject'] = "妈妈学院接口测试报告 "  
    main_msg['Date'] = email.Utils.formatdate( )  
  
    # 得到格式化后的完整文本 
    fullText = main_msg.as_string( )  
  
    # 用smtp发送邮件  
    try:  
        server.sendmail(From, To, fullText)  
    finally:  
        server.quit()  

