# How to install an airflow service for this project
This documentation shows how to install airflow in your AWS EC2 instance. It can be seperated into three parts. The detail of each part is listed below.
1. **PART ONE :** Install **MySql** as a database backend for airflow service. 
2. **PART TWO :** Install **AIRFLOW** service
3. **PART THREE :** Launch airflow service
-----
#### *PART ONE - Install **MySql** as a database backend for airflow service. 
**Step1:** Launch an AWS EC2 instance
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_01.png">
</p>  

**Step2:** SSH to this AWS EC2 instance
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_02.png">
</p>  

**Step3:** Update apt-get list
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_03.png">
</p>  

**Step4:** Install mysql-server
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_04.png">
</p>  

**Step5:** Install mysql-client
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_05.png">
</p>  

**Step6:** Install libmysqlclient-dev
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_06.png">
</p>  

**Step7:** Access to MySql database
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_07.png">
</p>  

**Step8:** Create a database which is called airflow
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_08.png">
</p>  

**Step9:** Create a user which is named airflow.
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_09.png">
</p>  

**Step10:** Give the user--'airflow' the right to access to this Mysql Database. It allows airflow to access to this database
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_10.png">
</p>  

**Step11:** Refresh the Mysql database to make the new setting work
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_11.png">
</p>  

**Step12:** Exit Mysql database
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_12.png">
</p>  

-----
#### *PART TWO - Install **AIRFLOW** service*
**Step1:** Install pip
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_13.png">
</p>  

**Step2:** Updata pip to the latest version
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_14.png">
</p>  

**Step3:** Install MySql-python package
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_15.png">
</p>  

**Step4:** Check whether we successfully install MySql-python package or not
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_16.png">
</p>  

**Step5:** Make a directory for airflow
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_17.png">
</p>  

**Step6:** Set the environment variable 
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_18.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_19.png">
</p>  

**Step7:** Install apache-airflow package
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_20.png">
</p>  

**Step8:** After finishing the installation of apache-airflow package, access to MySql database
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_21.png">
</p>  

**Step9:** Check explicit_default_for_timestamp
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_22.png">
</p>  

**Step10:** Check explicit_default_for_timestamp
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_22.png">
</p>  

**Step11:** Change explicit_default_for_timestamp setting from OFF to ON
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_24.png">
</p>  

**Step12:** Check explicit_default_for_timestamp again
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_25.png">
</p>  

**Step13:** Exit MySql database
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_26.png">
</p>

**Step14:** Find airflow.cfg
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_27.png">
</p>  

**Step15:** Modify airflow.cfg
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_28.png">
</p>

**Step16:** Find sql_alchmy_conn
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_29.png">
</p>

**Step17:** Modify sql_alchmy_conn
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_30.png">
</p>

**Step18:** Uninstall marshmallow-sqlalchemy (you only need to do this step if you use AWS EC2 instance with ubuntu 16.04)
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_31.png">
</p>  


**Step19:** Install marshmallow-sqlalchemy==0.17.1 (you only need to do this step if you use AWS EC2 instance with ubuntu 16.04)
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_32.png">
</p>  


#### *PART THREE - Launch airflow service*  

**Step1:** Launch the airflow backend MySql database
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_33.png">
</p>  

**Step2:** Launch airflow web server
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_34.png">
</p>  

**Step3:** Launch airflow scheduler
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_35.png">
</p>  

**Step2:** Access to airflow web server through port 8080
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/airflow_install_36.png">
</p>  

**Step4:** Congratulations. All the necessary steps for starting airflow are finished.