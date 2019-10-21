# import the necessary packages
import paramiko

# configuration for connecting to other AWS EC2 instance
pemfile_path = '.pem file'
target_ec2_ip = 'ip address'
target_ec2_username = 'ubuntu'
cmd = 'touch test.csv'

# connect to other AWS EC2 instance
key = paramiko.RSAKey.from_private_key_file(pemfile_path)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=target_ec2_ip, username=target_ec2_username, pkey=key)
stdin, stdout, stderr = client.exec_command(cmd)

# print the result 
print(stdout.read())
# close the connection
client.close()