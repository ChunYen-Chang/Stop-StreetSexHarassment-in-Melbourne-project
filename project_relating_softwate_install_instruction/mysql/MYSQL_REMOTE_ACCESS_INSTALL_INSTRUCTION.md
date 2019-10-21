# How to install a MySql database which allows the remote access  

This documentation shows how to install a MySql database which allows the remote accessAWS EC2 instance. The installation detail is listed below.  

-----
**Step1:** Update apt-get list
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_01.png">
</p>  

**Step2:** Install mysql-server and mysql-client
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_02.png">
</p>  

**Step3:** Access to MySql database
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_03.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_04.png">
</p> 

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_05.png">
</p> 

**Step4:** Give the privileges to remote user. This setting make them have the right to access to this database
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_06.png">
</p>  

**Step5:** Reflush the system to make the new setting work
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_07.png">
</p>  

**Step6:** Find the path of *my.cnf*
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_08.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_09.png">
</p>  

**Step7:** Modify *my.cnf* file. By modify this file, we bind the MySql DB to localhost. It allows other remote users access to this MySql database directly. 
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_10.png">
</p>  

**Step8:** Put *[mysqld] bind-address = 0.0.0.0* in this file
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_11.png">
</p>  

**Step9:** Restart the MySql server
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_12.png">
</p>  

**Step10:** Access to the MySql database again to see whether it works or not
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_13.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_14.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/mysql_install_15.png">
</p> 

**Step15:** Congratulations. All the necessary steps for installing a MySql DB which allows remote access are finished.