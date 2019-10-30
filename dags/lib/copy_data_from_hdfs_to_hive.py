# import the necessary packages
from pyhive import hive


# define functions
def show_hive_database(hive_server_ip, hive_server_port):
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
        # retrive file name from previous task through Xcom
        ti = kwargs['ti']
        file_name = ti.xcom_pull(task_ids=previous_task_id)
        hdfs_file_path = '/data/' + file_name

        # connect to hive
        conn = hive.connect(host=hive_server_ip, port=hive_server_port, username='root')
        cursor = conn.cursor()

        # upload fils from hdfs to hive
        upload_cmd = "load data inpath '" + hdfs_file_path + "' into table "+ database_name + "." + table_name
        cursor.execute(upload_cmd)

        # close the connection
        cursor.close()
        conn.close()

def execute_command_in_hive(hive_server_ip, hive_server_port, *args):
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
