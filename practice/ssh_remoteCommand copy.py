#  pip install paramiko  - before executing we need the library
#  it is passwd from real ubuntu remote machine and thar is located << file.docx >> file we should find
import paramiko

user_name = "ubuntu"
passwd = "2728"
ip = "3.17.174.166"

print("Please wait, creating ssh client...")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("Please wait, connecting with remoter server...")
ssh_client.connect(hostname=ip, username=user_name, password=passwd)
#  cmd = "cd folderForFile"
cmd_1 = "find . -name file.docx"

print("Please wait, executing command on remoter server...")
stdin, stdout, stderr = ssh_client.exec_command(cmd_1)

stdout = stdout.readlines()
print(stdout)
print("Successfully executed command on remoter !!!")
