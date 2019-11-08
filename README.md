
  
  
# Stop Street SexHarassment in MElbourne

#### *PROJECT BACKGROUND and DESCRIPTION*
What is the social problem in Melbourne CBD now? Different people may have different opinions. But, Based on the report from Australian 
Broadcasting Corporation News (ABC News), this report points that even the crime rate in Melbourne CBD has a going-down trend from 
2009 to 2018, the rate of sex crime (especially the street harassment rate)has risen every year since 2013 (Kerr, 2018). At the same 
time, Victoria Government recently released several advertisement to urge females to call out when they experience street sex 
harassment. (https://www.youtube.com/watch?v=UHxAxRYIlfE). Combining these two things, it shows that street harassment is a 
considerable social problem in Melbourne now. This project aims at finding a way to improving females safety in Melbourne CBD area.

To realize this street sex harassment problem in more detail, this project conducts several personal interviews with 21 females which 
lives in Melbourne CBD area. Based on these face-to-face interviews with these females, we find several important key factors. These 
factors are bar, restaurant, construction site, street light, the number of pedestrian. Our interviewees tell us that they have higher
probability to encounter a street sex harassment if they are close to bars, construction sites, and street with few street lights. 
Conversely, they have lower probability to encounter a street sex harassment if they are close to restaurants and area with many 
pedestrian. Therefore, **the main goal of this project is collecting data sets relating to bar's location in Melbourne CBD, construction 
site location in Melbourne CBD, restaurant's location in Melbourne CBD, location and number of street light in Melbourne CBD, 
the number of pedestrian at specific area in Melbourne CBD and put all these data sets in a well-managed data warehouse, non-SQL 
database, SQL database for other front-end website developers**. We hope these others front-end website developers employ this integrated 
data sets to build a MAP application which shows safe amd dangerous areas for females who live in Melbourne CBD so that these females 
can use this the application to avoid passing by some dangerous areas. **Another goal in this project is that we try to collect Twitter 
posts which are posted by people who live in Melbourne CBD area and the the twitter post which includes street sex harassment contents. 
And, load these twitter post in well-managed data warehouse, non-SQL database, SQL database** In our viewpoint, these twitter posts 
are valuable because the posts can be analyzed by experts to discover some other important factors which can reduce the probability 
that females encounter street sex harassment. We hope future experts can use the twitter posts we collect to do the following analyses 
to help females living in Melbourne CBD out of the street sex harassment threat. 

In sum, this project aims at finding a way to lower down the probability that females living in Melbourne CBD encounter a street sex 
harassment. To achieve this goal, this project collects data sets relating to CBD bar's location, CBD construction site location, 
CBD restaurant's location, CBD street light location and numbe, the number of pedestrian at specific area in Melbourne CBD and put 
all data sets in a well-managed data warehouse, non-SQL database, SQL database for others front-end website developers. Also, this 
project Twitter posts which are posted by people who live in Melbourne CBD area and the the twitter post which includes street sex 
harassment contents. Then, store these twitter post in a well-managed data warehouse, non-SQL database, SQL database for future experts 
to analyze.

#### *SYSTEM ARCHITECTURE*

<p align="center">
  <img width="1000" height="1600" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/system_architecture.jpeg">
</p>

OK, now you can check the system architecture picture above. Hmm....does it look complicated? No worries, we will take you walk 
through the whole system to make sure you understand what happens in this picture.  

First, let us take a look at the blue line. 
This blue line is the first data pipeline. The AWS EC2 extracts streaming Twitter posts from Twitter API and save these posts in 
a csv file at 1AM everyday . After the csv file is saved, the Apache flume will immediately move this csv file into HDFS. At 6am, 
the Apache airflow will move the the csv file data to HBASE and HIVE. After the csv is successfully loaded into Hive, the Apache Sqoop 
will take the job of moving the csv file data to MySQL database.  

Now, let us check the second data pipeline--the red line. This data pipeline will kick off at 6am everyday by Apache airflow. It starts 
with extracting pedestrian data (the number of perdestrian at a specific CBD area) from Melbourne Government API. After successfully 
extracting the pedestrian data, this data will move to HDFS. Then, this data will be moved from HDFS to HBASE and HIVE. Afterwards, 
the airflow will check whether the HIVE receives the data or not. If HIVE receives the data, airflow moves this data from HIVE to 
MySQL database by using sqoop.  

Finally, we are talking about the last data pipeline--the black line. This data pipeline will start at 6am on the **first day of each 
month** (this one is different than other two data pipeline). It starts with extracting bar location data, restaurant location data, 
construction site location data, streetlight number and location data from Melbourne Government API. After successfully 
extracting these datasets, all datasets will move to HDFS. Then, datasets will be moved from HDFS to HBASE and HIVE. Afterwards, 
the airflow will check whether the HIVE receives these datasets or not. If HIVE receives the datasets, airflow moves datasets from 
HIVE to MySQL database by using sqoop.  

  
Now we already finished the explanation for the above system architecture picture. We can talk about some questions you may have
when you read this part.
1. **Q1: Why do we apply different time schedule for the red data pipeline and black pipeline?**  

ANS: The reason is different datasets have different 
update intervals. Bar location, restaurant location, construction site location, street light number and location dataset will be updated 
every month. Pedestrian number dateset will be updated everyday.  

2. **Q2:I want to know the details of each datasets. Could you provide the relating information?**  

ANS: Yes, of course. You can check the picture below .

<p align="center">
  <img width="800" height="600" src="https://github.com/ChunYen-Chang/Stop-StreetSexHarassment-in-Melbourne-project/blob/master/image/datasets_table.jpeg">
</p>


------------
#### SOFTWATE VERSION IN THIS PROJECT
1. **HIVE version:** HIVE 2.3.5
2. **HBASE version:** HBASE 1.4.10
3. **SQOOP version:** SQOOP 1.4.7
4. **FLUME version:** FLUME 1.6.0
5. **AIRFLOW version:** AIRFLOW 1.10.6
6. **PYTHON version:** PYTHON 2.7 
7. **Hadoop version:** Hadoop 2.8.5
8. **MySql version:** MySql 5.7
9. **Ubuntu version for EC2 instance:** Ubuntu Server 16.04 LTS (HVM)
10. **.jar file for flume spool sink:** These .jar files should download hadoop-2.9.2 package, and extract from hadoop-2.9.2/bin
    1. hadoop-common-3.0.1.jar
    2. woodstox-core-5.0.3.jar
    3. stax2-api-3.1.4.jar
    4. commons-configuration2-2.1.1.jar
    5. hadoop-auth-3.0.1.jar 
    6. htrace-core4-4.1.0-incubating.jar 
    7. hadoop-hdfs-3.0.1.jar 

------------
#### FILES IN THE REPOSITORY
- **README.md**: It includes the project background, project description, system architecture, software version, and the information about how to run the project.  

- **image folder**: It contains images which are used in this repository  

- **project_relating_softwate_install_instruction**: It contains the information about how to install necessary softwares for this project.
    1. **airflow folder**: The detailed instruction(with pics) about how to install Apache Airflow in AWS EC2 instance for this project
    2. **aws_emr folder**: The detailed instruction(with pics) about how to launch an AWS EMR cluster for this project
    3. **flume folder**: The detailed instruction(with pics) about how to install Apache flume in AWS EC2 instance for this project
    4. **mysql folder**: The detailed instruction(with pics) about how to install MySQL in AWS EC2 instance for this project  

- **code**:  It includes all code for this project
    1. **dags folder**: This folder includes all codes of airflow part
        1. **data from API folder**: A folder which for keeping the datasets which are extracted from Melbourne Government API
        2. **key folder**: A folder which contains .pem file. This file is the key to connect to AWS EMR cluster
        3. **configuration folder**: A folder contains one configuration file. You can modify all parameters in this project(such as AWS_hdfs_masternode_ip) in this file.
        4. **lib folder**: A folder contains all python functions which are used in data pipelines
        5. **pipeline_bar_restaurant_construction_streetlight.py**: The data pipeline configuration for bar location, restaurant location, construction site location, streetlight location datasets 
        6. **pipeline_pedestrian.py**: The data pipeline configuration for pedestrian dataset 
        7. **pipeline_tweet.py**: The data pipeline configuration for tweet post dataset
    2. **hadoop folder**: This folder includes all codes of hadoop cluster part
        1. **Hadoop_cmd.txt**: The command of making directory in hdfs and modify the directory's access permission
        2. **Hbase_cmd.txt**: The command of creating talbes and dropping tables in Hbase
        3. **Hive_cmd.txt**: The command of creating database, creating talbes, and dropping tables in Hive
        4. **MySql_cmd.txt**: The command of creating database, creating talbes, and dropping tables in Mysql
    3. **flume folder**: This folder includes all codes of flume part
        1. **Twitter_data_extraction folder**: It includes python code of extracting data from Twitter API
        2. **flume**: It includes the flume configuration file


