# import the necessary packages
import paramiko


# define functions
def ssh_other_ec2_and_run_cmd(pemfile_path, target_ec2_ip, target_ec2_username, *args):
	key = paramiko.RSAKey.from_private_key_file(pemfile_path)
	
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=target_ec2_ip, username=target_ec2_username, pkey=key)
	
	for cmd in args:
		client.exec_command(cmd)

	client.close()







# configuration for connecting to other AWS EC2 instance
pemfile_path = '/home/ubuntu/20191021.pem'
target_ec2_ip = '54.203.19.110'
target_ec2_username = 'ubuntu'
cmd = 'touch a'


# connect to other AWS EC2 instance
key = paramiko.RSAKey.from_private_key_file(pemfile_path)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=target_ec2_ip, username=target_ec2_username, pkey=key)
stdin, stdout, stderr = client.exec_command(cmd)

print(stdout.read())

client.close()
