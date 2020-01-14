import paramiko

#  ==============================================================================================================||
user_name = "ubuntu"
password = "2728"
ip = "3.17.174.166"
#  ==============================================================================================================||
ssh = paramiko.SSHClient()  # ssh client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # for first connection to remote server
ssh.connect(hostname=ip, username=user_name, password=password, port=22)
#  ==============================================================================================================||
stdin, stdout, stderr = ssh.exec_command('../')
stdin, stdout, stderr = ssh.exec_command('free -m')
# stdin, stdout, stderr = ssh.exec_command('whoami')
# stdin, stdout, stderr = ssh.exec_command('whoami')
# stdin, stdout, stderr = ssh.exec_command('whoami')
# stdin, stdout, stderr = ssh.exec_command('whoami')

print("The output == POSITIVE == is: ")
print(stdout.readlines())

print("The output of == ERROR == is: ")
print(stderr.read())

ssh.close()  # after ssh client using we should to close ssh connection (god practice)
