# import the necessary packages
from pyhive import hive


# define functions
def show_hive_database(hive_server_ip, hive_server_port):
	'''
	Description: This function helps users to check the database information in Hive
	Parameters: -hive_server_ip: the ip address of your Hive master node
		    -hive_server_port: the port of your Hive master node
	Returns: None
	'''
	# connect to hive
	conn = hive.connect(host=hive_server_ip, port=hive_server_port, username='root')
	cursor = conn.cursor()

	# show all databases in hive
	cursor.execute("show databases")	
	print(cursor.fetchall())
	
	# close the connection
	cursor.close()
	conn.close()

def show_hive_table_data(hive_server_ip, hive_server_port, database_name, table_name):
        '''
        Description: This function helps user to check the table information in Hive
        Parameters: -hive_server_ip: the ip address of your Hive master node
                    -hive_server_port: the port of your Hive master node
		    -database_name: the database your table resides 
		    -table_name: the table you want to check 
        Returns: None
        '''
	# connect to hive
	conn = hive.connect(host=hive_server_ip, port=hive_server_port, username='root')
        cursor = conn.cursor()
	
	# show data in a specific table
	show_table_cmd = "SELECT * FROM " + database_name + "." +  table_name
	cursor.execute(show_table_cmd)
	print(cursor.fetchall())

	# close the connection
        cursor.close()
        conn.close()

def upload_data_to_hive_table(hive_server_ip, hive_server_port, database_name, table_name, previous_task_id, **kwargs):
	'''
        Description: This function helps users to upload data from Hdfs to Hive
        Parameters: -hive_server_ip: the ip address of your Hive master node
                    -hive_server_port: the port of your Hive master node
                    -database_name: the database your table resides
                    -table_name: the table you want to check
		    -previous_task_id: this parameter is used for airflow Xcom.
		     By having this parameter, this function can know which data
		     should load into the Hive.
        Returns: None
        '''
        # retrive file name from previous task through Xcom
        ti = kwargs['ti']
        file_name = ti.xcom_pull(task_ids=previous_task_id)
        hdfs_file_datafolder_path = '/data/' + file_name
	hdfs_file_flumefolder_path = '/flume/' + file_name

        # connect to hive
        conn = hive.connect(host=hive_server_ip, port=hive_server_port, username='root')
        cursor = conn.cursor()

	# choose different upload_cmd
	if 'tweet' in file_name:
		upload_cmd = "load data inpath '" + hdfs_file_flumefolder_path + "' into table "+ database_name + "." + table_name
	else:
		upload_cmd = "load data inpath '" + hdfs_file_datafolder_path + "' into table "+ database_name + "." + table_name

	# upload fils from hdfs to hive
        cursor.execute(upload_cmd)

        # close the connection
        cursor.close()
        conn.close()

def execute_command_in_hive(hive_server_ip, hive_server_port, *args):
	'''
        Description: This function gives users the freedom to execute the command they
		     like. They only have to type the command in the *args place, and
		     the command can be executed.
        Parameters: -hive_server_ip: the ip address of your Hive master node
                    -hive_server_port: the port of your Hive master node
		    -*args: commands users want to execute
        Returns: None
        '''
	# connect to hive
        conn = hive.connect(host=hive_server_ip, port=hive_server_port, username='root')
        cursor = conn.cursor()

	# execute the hive command
        if len(args) > 0:
                for hive_cmd in args:
                        cursor.execute(hive_cmd)

	# close the connection
        cursor.close()
        conn.close()
