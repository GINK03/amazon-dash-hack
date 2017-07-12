#! /usr/bin/python3
import os
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

SECRET = { x:y  for x,y in map(lambda x:x.split('='), filter(lambda x:x!='', open('/home/gimpei/private_configs/google_account1').read().split('\n') ) ) }
MAILS = { x:y  for x,y in map(lambda x:x.split('='), filter(lambda x:x!='', open('/home/gimpei/private_configs/mailaddrs').read().split('\n') ) ) }


msg = bytes("""
体調不良により、本日お休みをいただきたく思います。
どうぞよろしくお願いします。
""", 'utf8')
fromaddr = SECRET['GOOGLE_ACC']
toaddrs  = MAILS['KINTAI'] 

username = SECRET['GOOGLE_ACC']
password = SECRET['GOOGLE_PWD']
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
print('正常に送信が終了しました')
