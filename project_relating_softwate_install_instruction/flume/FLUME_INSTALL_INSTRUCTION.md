# How to install flume in AWS EC2 instance with Ubuntu 16.04 for this project 

This documentation shows how to install flume in AWS EC2 instance with Ubuntu 16.04 for this project in order to immediately move date 
from this AWS EC2 instance to AWS Hadoop cluster. This documentation can be seperated into two parts. The detail of each part is listed below.
1. **PART ONE :** Install Flume in the AWS EC2 instance. 
2. **PART TWO :** Configure corresponding settings in this EC2 instance for moving data to a hadoop cluster.  

-----
#### *PART ONE - Install **Flume** in the AWS EC2 instance. 
**Step1:** Update apt-get list
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_01.png">
</p>  

**Step2:** Install JAVA in this ec2 instance
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_02.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_03.png">
</p>  

**Step3:** Make sure you successfully install JAVA in this ec2 instance
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_04.png">
</p>  


**Step4:** Set the JAVA_HOME variable
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_05.png">
</p>   

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_06.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_07.png">
</p>  

**Step5:** Make sure you successfully configure the JAVA_HOME variable
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_08.png">
</p>  

**Step6:** Download flume (the bin and src file)
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_09.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_10.png">
</p>

**Step7:** Unzip these two flume files
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_11.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_12.png">
</p>  

**Step8:** Copy **apache-flume-1.6.2-src folder** to **apache-flume-1.6.2-bin** folder
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_13.png">
</p>  

**Step9:** Move **apache-flume-1.6.2-bin** folder to **/opt/flume** folder
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_14.png">
</p>  

**Step10:** Create a flume data pipeline configuration file
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_15.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_16.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_17.png">
</p>  


-----
#### *PART TWO - Configure corresponding settings in this EC2 instance for moving data to a hadoop cluster
**Step1:** Since in this project we are going to move data to a hadoop cluster, we need to install some hdfs relating .jar file in this 
server. Thus, let us download the Hadoop 2.9.2 package firstly.  
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_18.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_19.png">
</p>

**Step2:** Unzip the hadoop 2.9.2 file
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_20.png">
</p>  
  
**Step3:** Move the necessary .jar files to **/opt/flume/apache-flume-1.6.0-bin/lib**. It allows flume to use these .jar files 
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_21.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_22.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_23.png">
</p>  

**Step4:** Now, We already moved all the necessary .jar to flume bin folder. Then, we are going to write a python code for extracting data 
from Twitter API and saving the straming data in a **data folder**. So, Create a **tweet** directory in /home/ubuntu/ and change directory to 
this directory
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_24.png">
</p>  

**Step5:** Write the python code for getting data from twitter API
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_25.png">
</p>  
  
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_26.png">
</p> 

**Step6:** Create **tweet_api.txt** file and put your twitter access key information in this file
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_27.png">
</p>  

**Step7:** Create **data** directory in **/home/ubuntu/tweet** directory. This directory is for saving the streaming data from twitter API
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_28.png">
</p>  

**Step8:** OK, now we finish the python code for getting data from twitter API. We need to create a hadoop cluster in AWS (by using AWS EMR).  
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_30.png">
</p>  

**Step9:** Connect to the name node of this hadoop cluster  
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_31.png">
</p>  

**Step10:** Create a directory which is called **flume** in the hadoop cluster
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_32.png">
</p>  

**Step11:** Allow group and other have the right to write files in this **flume** directory
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_33.png">
</p>  

**Step12:** Make use we have the correct setting for this **flume** directory
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_34.png">
</p>  

**Step13:** Connect to the EC2 instance which we install the flume and modify the flume data pipeline configuration file (change the hadoop cluster name node 
IP address and the port--the port is 8020).
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_35.png">
</p>  

**Step14:** Start the python code for extracting data from Twitter API  
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_36.png">
</p>  

**Step15:** Start the flume service 
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_37.png">
</p>  
  
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_38.png">
</p>  

**Step16:** After we run the python code and start the flume service, we can connect to the hadoop cluster to see whether the data is sent to
this hadoop cluster or not. This following photo shows that the data is already sent to this hadoop cluster.
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/flume_install_39.png">
</p>  

**Step17:** Congratulations. All the necessary steps are finished.