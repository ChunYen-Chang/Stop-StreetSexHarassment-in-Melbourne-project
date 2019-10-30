# import the necessary packages
from hdfs.client import Client


# define functions
def make_directory(hdfs_address, directory_path, directory_name):
	client = Client(hdfs_address)
	client.makedirs(directory_path + directory_name)

def upload_data(hdfs_address, previous_task_id, **kwargs):
	# retrive file name from previous task through Xcom 
	ti = kwargs['ti']
	file_name = ti.xcom_pull(task_ids=previous_task_id)	
	local_file_path = '/home/ubuntu/airflow/dags/data_from_API/' + file_name
	hdfs_file_path = '/data/' + file_name

	# connect to hdfs
	client = Client('http://' + hdfs_address)

	# upload the file
	client.upload(hdfs_file_path, local_file_path)

def list_files(hdfs_address, hdfs_file_path):
	# connect to hdfs
	client = Client(hdfs_address)

	# list all folders
	client.list(hdfs_file_path)
