import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

smtp_server_name = "smtp.gmail.com"
port = 587
sender_email = "kiralymatyas888@gmail.com"
receiver_email = "kiralymatyas888@gmail.com"
password = input('Enter your password: ')

# Create a secure SSL context
context = ssl.create_default_context()

try:
    smtp_server = smtplib.SMTP(smtp_server_name, port)
    smtp_server.starttls(context=context)
    smtp_server.login(user=sender_email,password=password)
    msg = MIMEMultipart('mixed')
    msg['Subject'] = 'Test HTML Email'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    fullpath = []
    #path = r'/home/peter/Documents/' # there was a problem with the os library, it could execute the listdir method
    fullpath.append('/home/peter/Documents/mail_')
    fullpath.append('/home/peter/Documents/Moai_Rano_raraku.jpg')

    for x in fullpath:
        attachment = open(x,'rb')
        part0 = MIMEBase('application', 'octet-stream')
        part0.set_payload(attachment.read())
        encoders.encode_base64(part0)
        part0.add_header('Content-Disposition', 'attachement ; filename = ' + x.split("/")[-1])
        msg.attach(part0)

    plain_text = 'Part 1 : This is the plain text part of the email. Check out the attachment I sent. It could not only be a document but picture or other files.'
    html_text = '<p> <b> Part 2 :</b> <br>  This is the html part of the email. </p>'

    part1 = MIMEText(plain_text, 'plain')
    part2 = MIMEText(html_text, 'html')

    msg.attach(part1)
    msg.attach(part2)

    smtp_server.sendmail(from_addr=sender_email,to_addrs=receiver_email, msg=msg.as_string())
    smtp_server.quit()

except smtplib.SMTPException as e:
    print(e)


