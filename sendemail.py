import glob
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = dets.readline()
email_password = dets.readline()
email_send = dets.readline()

subject = 'Your new E-book'
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
part = MIMEBase('application','octet-stream')

body = 'Hi there, sending this ebook from Python!'
msg.attach(MIMEText(body,'plain'))

filename=glob.glob('/home/pi/Documents/Conv_PDFs/*.mobi')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)
	
for file in filename:
	attachment = open(file,'rb')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	fname = os.path.basename(file)
	part.add_header('Content-Disposition',"attachment; filename= "+fname)
	msg.attach(part)

text = msg.as_string()
	
server.sendmail(email_user,email_send,text)
server.quit()

for file in filename:
	subprocess.call('rm',file)
	
print "Sending email done"
