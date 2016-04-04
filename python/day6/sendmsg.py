#coding: utf-8
import smtplib
from email.mime.text import MIMEText
me='bezginmysvc@gmail.com'
you='mbizzi@ukr.net'
text='Тестовое письмо'+'\n'+'Отправка письма из python'
subj='Тестовое письмо'

server='smtp.gmail.com'
port=25
user_name='bezginmysvc@gmail.com'
user_passwd='Altera1545'
msg=MIMEText (text, "", "utf-8")
msg['Subject'] = subj
msg['From']=me
msg['To']=you

s=smtplib.SMTP(server,port)
s.ehlo()
s.starttls()
s.ehlo()
s.login(user_name, user_passwd)
s.sendmail(me, you, msg.as_string())
s.quit()
