# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:00:36 2017

@author: LDH
"""

# email_sender.py
from email.header import Header
from email.mime.text import MIMEText
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
    
if __name__ == '__main__':
    send_email()
