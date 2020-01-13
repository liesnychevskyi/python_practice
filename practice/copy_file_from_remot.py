import paramiko

user_name = "ubuntu"
passwd = "2728"
ip = "3.17.174.166"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=ip, username=user_name, password=passwd, port=22)
sftp_client = ssh.open_sftp()
#sftp_client.get('/home/ubuntu/folderForFile/file.txt',
#                'C:\\Users\\User\\PycharmProjects\\python_practice\\staff_for_identifying\\dir_0\\bugg_0.py')

cmd_1 = "find . -name file.docx"
cmd_2 = "ls"
cmd_3 = "cd /home/ubuntu/folderForFile/"

print("Please wait, executing command on remoter server...")
stdin, stdout, stderr = ssh.exec_command(cmd_3)
stdin, stdout, stderr = ssh.exec_command(cmd_2)
stdout = stdout.readlines()
print(stdout)

sftp_client.close()
ssh.close()
