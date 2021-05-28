import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_id = 'mndabeni6@gmail.com'
receiver_email_id = input('Please Enter Your Email_Address: ')
password = input('Please Enter your password: ')
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = receiver_email_id
msg['Subject'] = subject
body = "Hello everyone how are you doing, i am doing fine"
body =  body + "How was your task yesterday"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
s.login(sender_email_id, password)
s.sendmail(sender_email_id, receiver_email_id, text)
s.quit()
