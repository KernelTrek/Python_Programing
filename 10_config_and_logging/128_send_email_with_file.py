
from email import message
from email.mime import multipart
from email.mime import text
import smtplib

#import config

smtp_host= 'smtp.live.com'
smtp_port= 587

from_email = 'xxxx@hotmail.com'
to_email = 'xxxx@hotmail.com'
username = 'xxxx@hotmail.com'
password = 'werwerwerew'
#
# from_email = config.from_email
# to_email = config.to_mail
# username = config.username
# password = config.password

msg = multipart.MIMEMultipart()

msg = message.EmailMessage()
#msg.set_content('Test email')
msg['Subject'] = 'Test mail sub'
msg['From'] = from_email
msg['To'] = to_email

# 파일 추가 부분 [메세지]
msg.attach(text.MIMEText('Test email', 'plain'))

# 파일 추가 [ 파일]
with open('128_send_email_with_file.py', r) as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='lesson.txt'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
# smtp 동작 여부 확인
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()