import base64
import paramiko

hostname = 'etrans.wmg.com'
password = 'welcome123'
destination = '/wmi7digital'
username = 'wmi7digital'
port = '22'


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,port=port,username=username,password=password)

sftp = ssh.open_sftp()
sftp.chdir('/wmi7digital/Archive')
x = sftp.listdir()

ssh.close()

print(len(x))
