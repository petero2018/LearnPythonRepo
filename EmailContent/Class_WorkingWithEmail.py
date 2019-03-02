import smtplib, ssl
import codecs
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


class Email:

    def __init__(self, smtp_server_name, port):

        self.smtp_server_name = smtp_server_name
        self.port = port
        self.context = ssl.create_default_context()
        self.smtp_server = smtplib.SMTP(self.smtp_server_name, self.port)
        self.smtp_server.starttls(context=self.context)

    def send_email(self, sender_email, receiver_email, subject_email, messagetype, *attachmentpaths):

        try:
            password = input('Enter your password to your email account: ')
            self.smtp_server.login(user=sender_email,password=password)
            sender_email = sender_email
            receiver_email = receiver_email

            msg = MIMEMultipart('mixed')
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject_email

            if attachmentpaths:

                for attachmentpath in attachmentpaths:

                    attachment = open(attachmentpath,'rb')
                    part0 = MIMEBase('application', 'octet-stream')
                    part0.set_payload(attachment.read())
                    encoders.encode_base64(part0)
                    part0.add_header('Content-Disposition', 'attachement ; filename = ' + attachmentpath.split("/")[-1])
                    msg.attach(part0)
            else:
                print('No attachment')

            if messagetype == 'text':

                plain_text = open('Text_Email', 'r').read()
                part1 = MIMEText(plain_text, 'plain')
                msg.attach(part1)

            elif messagetype == 'html':

                html_text = codecs.open("HTML_Email.html", 'r', 'utf-8').read()
                part2 = MIMEText(html_text, 'html')
                msg.attach(part2)

            elif messagetype == 'both':

                plain_text = open('Text_Email', 'r').read()
                part1 = MIMEText(plain_text, 'plain')
                msg.attach(part1)

                html_text = codecs.open("HTML_Email.html", 'r', 'utf-8').read()
                part2 = MIMEText(html_text, 'html')
                msg.attach(part2)

            else:

                raise Exception('No such message type: {}'.format(messagetype))

            self.smtp_server.sendmail(from_addr=sender_email,to_addrs=receiver_email, msg=msg.as_string())
            self.smtp_server.quit()

            print('Message sent')

        except smtplib.SMTPException as e:
            print(e)


if __name__ == "__main__":

    SendEmail1 = Email(smtp_server_name="smtp.gmail.com", port=587)
    x = ['/home/peter/Documents/Moai_Rano_raraku.jpg', '/home/peter/Documents/mail_']
    SendEmail1.send_email('kiralymatyas888@gmail.com','kiralymatyas888@gmail.com', 'This is a test email with attachement','text', *x)
