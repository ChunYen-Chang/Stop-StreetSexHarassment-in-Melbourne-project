# import necessary packages
import configparser
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import PythonOperator
from lib import extract_data_from_API
from lib import copy_data_from_local_to_hdfs
from lib import copy_data_from_hdfs_to_hive
from lib import copy_data_to_hbase_and_mysql


# load configuration file for extracting settings which will be used in this data pipeline
config = configparser.ConfigParser()
config.read('/home/ubuntu/airflow/dags/configuration/project.cfg')
AWS_hdfs_masternode_ip = config.get('conf', 'AWS_hdfs_masternode_ip').encode('utf-8')
AWS_pemfile_path = config.get('conf', 'AWS_pemfile_path').encode('utf-8')
AWS_hbase_masternode_ip = config.get('conf', 'AWS_hbase_masternode_ip').encode('utf-8')
AWS_hbase_masternode_username = config.get('conf', 'AWS_hbase_masternode_username').encode('utf-8')
AWS_hive_server_ip = config.get('conf', 'AWS_hive_server_ip').encode('utf-8')
AWS_hive_server_port = int(config.get('conf', 'AWS_hive_server_port').encode('utf-8'))
AWS_hive_database_name = config.get('conf', 'AWS_hive_database_name').encode('utf-8')
AWS_hive_server_username = config.get('conf', 'AWS_hive_server_username').encode('utf-8')
AWS_mysql_ip = config.get('conf', 'AWS_mysql_ip').encode('utf-8')
AWS_mysql_port = config.get('conf', 'AWS_mysql_port').encode('utf-8')
AWS_mysql_user = config.get('conf', 'AWS_mysql_user').encode('utf-8')
AWS_mysql_pw = config.get('conf', 'AWS_mysql_pw').encode('utf-8')
      

# airflow dags setting
default_args = {
    'owner': 'ChunYen-Chang',
    'start_date': datetime(2019, 1, 1),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('stop_sex_harassment_project_tweet_dag',
          default_args=default_args,
          description='the data pipeline for tweet dataset',
          schedule_interval='0 6 * * *',
          catchup=False,
          max_active_runs=1
        )

# airflow tasks in this data pipeline
start_operator = DummyOperator(
    task_id='Begin_execution',  
    dag=dag
)

end_operator = DummyOperator(
    task_id='End_execution',
    dag=dag
)

get_tweet_filename_from_flume_directory = PythonOperator(
    task_id='get_tweet_filename_from_flume_directory_task',
    python_callable=copy_data_from_local_to_hdfs.list_files_in_flume_directory,
    op_kwargs={
        'hdfs_address': AWS_hdfs_masternode_ip,
    },
    dag=dag)

TWEETdata_hdfs_to_hbase = PythonOperator(
    task_id='TWEETdata_hdfs_to_hbase_task',
    python_callable=copy_data_to_hbase_and_mysql.copy_data_from_hdfs_to_hbase,
    op_kwargs={
        'pemfile_path': AWS_pemfile_path,
        'hbase_masternode_ip': AWS_hbase_masternode_ip,
        'hbase_masternode_username': AWS_hbase_masternode_username,
        'previous_task_id': 'get_tweet_filename_from_flume_directory_task'
    },
    provide_context=True,
    dag=dag)

TWEETdata_hdfs_to_hive = PythonOperator(
    task_id='TWEETdata_hdfs_to_hive_task',
    python_callable=copy_data_from_hdfs_to_hive.upload_data_to_hive_table,
    op_kwargs={
        'hive_server_ip': AWS_hive_server_ip,
        'hive_server_port': AWS_hive_server_port,
        'database_name': AWS_hive_database_name,
        'table_name': 'tweet',
        'previous_task_id': 'get_tweet_filename_from_flume_directory_task'
    },
    provide_context=True,
    dag=dag)

TWEETdata_hive_to_Mysql = PythonOperator(
    task_id='TWEETdata_hive_to_Mysql_task',
    python_callable=copy_data_to_hbase_and_mysql.copy_data_from_hive_to_mysql,
    op_kwargs={
        'pemfile_path': AWS_pemfile_path,
        'hive_server_ip': AWS_hive_server_ip,
        'hive_server_username': AWS_hive_server_username,
        'mysql_ip': AWS_mysql_ip,
        'mysql_port': AWS_mysql_port,
        'mysql_user': AWS_mysql_user,
        'mysql_pw': AWS_mysql_pw,
        'previous_task_id': 'get_tweet_filename_from_flume_directory_task'
    },
    provide_context=True,
    dag=dag)

# define the airflow dag
start_operator >> get_tweet_filename_from_flume_directory >> TWEETdata_hdfs_to_hbase >> TWEETdata_hdfs_to_hive >> TWEETdata_hive_to_Mysql >> end_operator




