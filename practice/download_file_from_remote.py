#  pip install paramiko  - before executing we need the library
#  it is passwd from real ubuntu remote machine and thar is located << file.docx >> file we should find
import paramiko
# ---------------------------------------------------------------------||
user_name = "ubuntu"
passwd = "2728"
ip = "3.17.174.166"
# ---------------------------------------------------------------------||
print("Please wait, creating ssh client...")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Please wait, connecting with remoter server...")
ssh_client.connect(hostname=ip, username=user_name, password=passwd)
sftp_client = ssh_client.open_sftp()  # open SFTP client - for remote transferring files or directories
# ---------------------------------------------------------------------|| Transfer from remote to local machine
print(dir(sftp_client))  # list of SFTP commands (operation)
# sftp_client.get('/home/ubuntu/remote_data/bug_0.txt', '/Users/Stan/PycharmProjects/python_practice'
#                                                       '/staff_for_identifying/dir_0/paramiko_download_from_remote.txt')
# sftp_client.chdir("/home/ubuntu")  # change dir by PARAMIKO on remote machine
# print(sftp_client.getcwd())  # print current dir location
# sftp_client.get('bug_big.txt', '/Users/Stan/PycharmProjects/python_practice'
#                                                       '/staff_for_identifying/dir_0/BIG_BUG.txt')
# ---------------------------------------------------------------------||Transfer from local to remote machine
sftp_client.put('/Users/Stan/PycharmProjects/python_practice/staff_for_identifying/dir_0/bugg_0.py',
                '/home/ubuntu/FROM_MY_MAC.py')
# ---------------------------------------------------------------------|| Close all connections
sftp_client.close()  # close SFTP client after using
ssh_client.close()  # close SSH client after using
# ---------------------------------------------------------------------||















