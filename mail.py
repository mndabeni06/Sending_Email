import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
sender_mail_id = 'mndabeni6@gmail.com'
receiver_mail_id = 'mpendulokhozamk2@gmail.com'
password = input("Enter sender mail password: ")

s.starttls()

s.login(sender_mail_id, password)

message = "Hello i love Python"
message = message +  "How is Python to your side?"
s.sendmail(sender_mail_id, receiver_mail_id, message)
s.quit()


