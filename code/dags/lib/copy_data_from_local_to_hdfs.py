# import the necessary packages
from hdfs.client import Client


# define functions
def make_directory(hdfs_address, directory_path, directory_name):
	'''
        Description: This function helps users to create a directory in hdfs
        Parameters: -hdfs_address: hadoop master node ip address
                    -directory_path: the path the user want to create a directory
		    -directory_name: the directory name
        Returns: None
        '''
	client = Client('http://' + hdfs_address)
	client.makedirs(directory_path + directory_name)

def upload_data(hdfs_address, previous_task_id, **kwargs):
	'''
        Description: This function helps users to upload a file from local to hdfs
        Parameters: -hdfs_address:  hadoop master node ip address
		    -previous_task_id: this parameter is used for airflow Xcom.
		     By having this parameter, this function can know which data
		     should load into hdfs.
        Returns: None
        '''
	# retrive file name from previous task through Xcom 
	ti = kwargs['ti']
	file_name = ti.xcom_pull(task_ids=previous_task_id)	
	local_file_path = '/home/ubuntu/airflow/dags/data_from_API/' + file_name
	hdfs_file_path = '/data/' + file_name

	# connect to hdfs
	client = Client('http://' + hdfs_address)

	# upload the file
	client.upload(hdfs_file_path, local_file_path)

def list_files_in_flume_directory(hdfs_address):
	'''
        Description: This function helps users to check files in a specific hdfs
		     directory
        Parameters: -hdfs_address: hadoop master node ip address
                    -hdfs_file_path: the hdfs directory path 
        Returns: files_utf8_encode. A list which contains all files' name in a 
		 directory
        '''
	# connect to hdfs
	client = Client('http://' + hdfs_address)

	# list all folders
	files =	client.list('/flume')
	files_utf8_encode = map(lambda x: x.encode('utf-8'), files)
	if len(files_utf8_encode) > 1:
		print('Please check the data pipeline, the number of files should be 1')
	else:
		print(files_utf8_encode[0])
		return files_utf8_encode[0]	


