# -*- coding: utf-8 -*-
# import the necessary packages
import paramiko


# define the hbase_cmd and sqoop_cmd dictionary
hbase_cmd = {
'bar': "sudo hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=',' -Dimporttsv.columns='HBASE_ROW_KEY,cf:trading_name, cf:census_year, cf:address, cf:area, cf:patrons, cf:lat, cf:lon' bar ",
'construction':"sudo hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=',' -Dimporttsv.columns='HBASE_ROW_KEY,cf:development_key, cf:status, cf:area, cf:address, cf:floor, cf:car_space, cf:lat, cf:lon' construction ",
'pedestrian':"sudo hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=',' -Dimporttsv.columns='HBASE_ROW_KEY,cf:sensor_id, cf:sensor_name, cf:sensor_description, cf:sensor_status, cf:lat, cf:lon, cf:date, cf:time, cf:pedestrain_num' pedestrian ",
'restaurant':"sudo hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=',' -Dimporttsv.columns='HBASE_ROW_KEY,cf:trading_name, cf:census_year, cf:address, cf:area, cf:seats, cf:lat, cf:lon' restaurant ",
'streetlight':"sudo hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=',' -Dimporttsv.columns='HBASE_ROW_KEY,cf:asset_number, cf:asset_description, cf:lamp_type_lupvalue, cf:lamp_rating_w, cf:mounting_type_lupvalue, cf:lat, cf:lon' streetlight "
}

sqoop_cmd = {
'bar': "sqoop export --connect jdbc:mysql://{}:{}/melproject --username {} --password {} --table bar --export-dir /user/hive/warehouse/melproject.db/bar/{} --update-key Datetime_row_index --update-mode allowinsert",
'construction': "sqoop export --connect jdbc:mysql://{}:{}/melproject --username {} --password {} --table construction --export-dir /user/hive/warehouse/melproject.db/construction/{} --update-key Datetime_row_index --update-mode allowinsert",
'pedestrian': "sqoop export --connect jdbc:mysql://{}:{}/melproject --username {} --password {} --table pedestrian --export-dir /user/hive/warehouse/melproject.db/pedestrian/{} --update-key Datetime_row_index --update-mode allowinsert",
'restaurant': "sqoop export --connect jdbc:mysql://{}:{}/melproject --username {} --password {} --table restaurant --export-dir /user/hive/warehouse/melproject.db/restaurant/{} --update-key Datetime_row_index --update-mode allowinsert",
'streetlight': "sqoop export --connect jdbc:mysql://{}:{}/melproject --username {} --password {} --table streetlight --export-dir /user/hive/warehouse/melproject.db/streetlight/{} --update-key Datetime_row_index --update-mode allowinsert"
}


# define functions
def ssh_to_other_ec2_and_run_bash_cmd(pemfile_path, target_ec2_ip, target_ec2_username, *args):
	key = paramiko.RSAKey.from_private_key_file(pemfile_path)
	
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=target_ec2_ip, username=target_ec2_username, pkey=key)
	
	for cmd in args:
		client.exec_command(cmd)

	client.close()

def copy_data_from_hdfs_to_hbase(pemfile_path, hbase_masternode_ip, hbase_masternode_username, previous_task_id, **kwargs):
        key = paramiko.RSAKey.from_private_key_file(pemfile_path)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hbase_masternode_ip, username=hbase_masternode_username, pkey=key)

        # retrive file name from previous task through Xcom
        ti = kwargs['ti']
        file_name = ti.xcom_pull(task_ids=previous_task_id)
        hdfs_file_path = '/data/' + file_name
	
	# check hbase_cmd dictionary and extract the command
	if 'bar' in hdfs_file_path:
		cmd = hbase_cmd['bar'] + hdfs_file_path
	elif 'construction' in hdfs_file_path:
		cmd = hbase_cmd['construction'] + hdfs_file_path
	elif 'restaurant' in hdfs_file_path:
		cmd = hbase_cmd['restaurant'] + hdfs_file_path
	elif 'streetlight' in hdfs_file_path:
		cmd = hbase_cmd['streetlight'] + hdfs_file_path
	elif 'pedestrian' in hdfs_file_path:
		cmd = hbase_cmd['pedestrian'] + hdfs_file_path

	# execute the command and terminate the conection
	client.exec_command(cmd)
	client.close()

def copy_data_from_hive_to_mysql(pemfile_path, hive_server_ip, hive_server_username, mysql_ip, mysql_port, mysql_user, mysql_pw, previous_task_id,**kwargs):
        key = paramiko.RSAKey.from_private_key_file(pemfile_path)

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hive_server_ip, username=hive_server_username, pkey=key)

        # retrive file name from previous task through Xcom
        ti = kwargs['ti']
        file_name = ti.xcom_pull(task_ids=previous_task_id)

        # check hbase_cmd dictionary and extract the command
	if 'bar' in file_name:
		cmd = sqoop_cmd['bar'].format(mysql_ip, mysql_port, mysql_user, mysql_pw, file_name)
	elif 'construction' in file_name:
		cmd = sqoop_cmd['construction'].format(mysql_ip, mysql_port, mysql_user, mysql_pw, file_name)
	elif 'restaurant' in file_name:
		cmd = sqoop_cmd['restaurant'].format(mysql_ip, mysql_port, mysql_user, mysql_pw, file_name)
	elif 'streetlight' in file_name:
		cmd = sqoop_cmd['streetlight'].format(mysql_ip, mysql_port, mysql_user, mysql_pw, file_name)
	elif 'pedestrian' in file_name:
		cmd = sqoop_cmd['pedestrian'].format(mysql_ip, mysql_port, mysql_user, mysql_pw, file_name)
	# execute the command and terminate the conection
	client.exec_command(cmd)
        client.close()

