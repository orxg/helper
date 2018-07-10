# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:00:36 2017

@author: LDH
"""

# email_sender.py
import os
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart,MIMEBase
from email.utils import formataddr
import smtplib

from_addr = 'vectortrader@163.com'
password = 'vectortrader2017'
to_addr = '343091787@qq.com'
privilege_password = 'vectortrader123'
smtp_server = 'smtp.163.com'
msg = 'Refresh failed'

def send_email(from_addr = from_addr,password = privilege_password ,
               to_addr = to_addr,smtp_server = smtp_server,
               msg = msg):
    '''
    发送邮件。   
    
    Parameters
    ----------
    from_addr
        发信地址
    password
        登录密码
    to_addr
        收信地址
    smtp_server
        smtp服务器地址
    msg
        str 发送内容
    '''
    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    msg = MIMEText(msg,'plain','utf8')
    
    # header
    from_ = formataddr((Header('vectortrader','utf8').encode(),from_addr))
    
    # to
    to_ = formataddr((Header('user','utf8').encode(),to_addr))
    
    # subject
    subject_ = Header('信息推送','utf8').encode()
    
    # 发送邮件
    
    msg['From'] = from_
    msg['To'] = to_
    msg['Subject'] = subject_
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()

#%% 发送带附件的邮件
def send_email_with_attachment(from_addr = from_addr,password = privilege_password,
               to_addr = to_addr,smtp_server = smtp_server,
               msg_text = None,attachment_type = None,file_name = None):
    '''
    发送邮件。   
    
    Parameters
    ----------
    from_addr
        发信地址
    password
        登录密码
    to_addr
        收信地址
    smtp_server
        smtp服务器地址
    msg_text
        str 发送内容
    attachment_type
        str 发送附件的MIME类型,图片为image,csv文件为application
    file_name
        str 发送附件所在地址
    '''
    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    msg_main = MIMEMultipart()
    
    msg_text = MIMEText(msg_text,'plain','utf8')
    msg_main.attach(msg_text)
    
    with open(file_name,'rb') as f:
        attachment = MIMEBase(attachment_type,os.path.splitext(file_name)[-1][1:],
                              filename = file_name)
        attachment.add_header('Content-Disposition','attachment',filename = file_name)
        attachment.add_header('Content-ID', '<0>')
        attachment.add_header('X-Attachment-Id', '0')
        attachment.set_payload(f.read())
        encoders.encode_base64(attachment)    
    msg_main.attach(attachment)
    
    # header
    from_ = formataddr((Header('vectortrader','utf8').encode(),from_addr))
    
    # to
    to_ = formataddr((Header('user','utf8').encode(),to_addr))
    
    # subject
    subject_ = Header('信息推送','utf8').encode()
    
    # 发送邮件
    
    msg_main['From'] = from_
    msg_main['To'] = to_
    msg_main['Subject'] = subject_
    server.sendmail(from_addr,[to_addr],msg_main.as_string())
    server.quit()

if __name__ == '__main__':
    send_email_with_attachment(msg_text = 'hahaha',attachment_type = 'application',
                               file_name = 'test.csv')
