#  pip install paramiko  - before executing we need the library
#  it is password from real ubuntu remote machine and thar is located << file.docx >> file we should find
import paramiko

user_name = "ubuntu"
password = "2728"
ip = "3.17.174.166"

print("Please wait, creating ssh client...")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("Please wait, connecting with remoter server...")
ssh_client.connect(hostname=ip, username=user_name, password=password)
#  cmd = "cd folderForFile"
cmd_1 = "find . -name file.docx"
cmd_2 = "cd .."
cmd_3 = "ls"
print("Please wait, executing command on remoter server...")
stdin, stdout, stderr = ssh_client.exec_command(cmd_3)

stdout = stdout.readlines()
print(stdout)
print("Successfully executed command on remoter !!!")

ssh_client.close()
