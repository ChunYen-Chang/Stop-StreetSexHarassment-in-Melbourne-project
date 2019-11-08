# Launch an AWS EMR Hadoop Cluster for this project  

This documentation shows how to start an AWS EMR cluster with HDFS, HIVE, HBASE, and SQOOP for this project. The detail steps are listed below.  

-----
**Step1:** Log in your AWS accound and find the EMR service
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_01.png">
</p>  

**Step2:** On EMR service page, click "Create cluster"
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_02.png">
</p>  

**Step3:** Click "Go to advanced options"
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_03.png">
</p>  

**Step4:** Click softwares this project need--"Hadoop 2.8.5, Hive 2.3.5, Hbase 1.4.10, Sqoop 1.4.7". Then, click Next to got the Hardware configuration Page
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_04.png">
</p>  

**Step5:** Use the default setting. Then, click Next to go to the General Cluster settings page
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_05.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_06.png">
</p> 

**Step6:** Use the default setting. Click Next to go to the Security Page
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_07.png">
</p>  

**Step7:** Use the default setting. Click Create cluster to stare the process of launching a EMR cluster
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_08.png">
</p> 

**Step8:** Go back to AWS EMR service page, you can see the AWS EMR is launching
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_09.png">
</p> 

**Step9:** Go to EC2 dashboard page, and find the name node and data node EC2 instance
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_10.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_12.png">
</p> 

**Step10:** Change the inbound rules in security group setting for these name node and data node. It allows us to access to the name node and data nodes from other EC2 instance
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_11.png">
</p>  

<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_13.png">
</p> 

**Step11:** Go back to AWS EMR service page. If you see the green running word appears on the screen, your AWS EMR cluster is ready
<p align="center">
  <img width="800" height="500" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/aws_launch_14.png">
</p> 

**Step12:** Congratulations. All the necessary steps for launching an AWS EMR cluster are finished.