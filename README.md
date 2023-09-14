# Project: STEDI Human Balance Analytics

## 1. Project Overview

### 1-1. Spark and Human Balance

This project will use Spark and AWS Glue to process data from multiple sources, categorize the data, and curate it to be queried in the future for multiple purposes, beyond that to write additional AWS Glue jobs to create curated step trainer data that can be used for machine learning.

### 1-2. Project Introduction: STEDI Human Balance Analytics

In this project, act as a data engineer for the STEDI team to build a data lakehouse solution for sensor data that trains a machine learning model.

Several customers have already received their Step Trainers, installed the mobile application, and begun using them together to test their balance. The Step Trainer is just a motion sensor that records the distance of the object detected. The app uses a mobile phone accelerometer to detect motion in the X, Y, and Z directions. The STEDI team wants to use the motion sensor data to train a machine learning model to detect steps accurately in real-time. Privacy will be a primary consideration in deciding what data can be used. Some of the early adopters have agreed to share their data for research purposes. Only these customers’ Step Trainer and accelerometer data should be used in the training data for the machine learning model.

## 2. Environments

### 2-1. Project Environment

- Python and Spark
- AWS Glue
- AWS Athena
- AWS S3

### 2-2. AWS Glue Configuration

#### Configuring the S3 VPC Gateway Endpoint

![Configuration](../l3_Using Spark & Data Lakes in the AWS Cloud/images/c3-l3-03.png)

- S3 VPC Gateway Endpoint
	- Step 1: Creating an S3 Bucket
	```
	aws s3 mb s3://bucket name
	```
	- tep 2: S3 Gateway Endpoint
	```
	aws ec2 describe-vpcs
	```
- Routing Table
```
aws ec2 describe-route-tables
```
- Create an S3 Gateway Endpoint
```
aws ec2 create-vpc-endpoint --vpc-id _______ --service-name 
com.amazonaws.us-east-1.s3 --route-table-ids _______
```
- 

#### Creating the Glue Service Role

![Configuration-2](../l3_Using Spark & Data Lakes in the AWS Cloud/images/c3-l3-02.png)

- Creating the Glue Service IAM Role
```
aws iam create-role --role-name zc-glue-service-role2 --assume-role-policy-document 
'{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "glue.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}'
```
- Grant Glue Privileges on the S3 Bucket
	- S3Access
	- GlueAccess

### 2-3. Workflow Environment Configuration

creating Python scripts using AWS Glue and Glue Studio. These web-based tools and services contain multiple options for editors to write or generate Python code that uses PySpark. 

## 3. Project Data

### **1. Customer Records**

Contains the following fields:

- serialnumber
- sharewithpublicasofdate
- birthday
- registrationdate
- sharewithresearchasofdate
- customername
- email
- lastupdatedate
- phone
- sharewithfriendsasofdate

### **2. Step Trainer Records (data from the motion sensor):**

Contains the following fields:

- sensorReadingTime
- serialNumber
- distanceFromObject

### **3. Accelerometer Records (from the mobile app):**

Contains the following fields:

- timeStamp
- user
- x
- y
- z

## 4. Project Requirements

To simulate the data coming from the various sources, you will need to create your own S3 directories for customer_landing, step_trainer_landing, and accelerometer_landing zones, and copy the data there as a starting point.

- Creating two Glue tables for the two landing zones. Share your customer_landing.sql and your accelerometer_landing.sql
- Query those tables using Athena, and take a screenshot of each one showing the resulting data. Name the screenshots customer_landing(.png,.jpeg, etc.) and accelerometer_landing(.png,.jpeg, etc.).

The Data Science team has done some preliminary data analysis and determined that the Accelerometer Records each match one of the Customer Records. They would like to create 2 AWS Glue Jobs:

- Sanitize the Customer data from the Website (Landing Zone) and only store the Customer Records who agreed to share their data for research purposes (Trusted Zone), creating a Glue Table called customer_trusted.
- Sanitize the Accelerometer data from the Mobile App (Landing Zone), and only store Accelerometer Readings from customers who agreed to share their data for research purposes (Trusted Zone), creating a Glue Table called accelerometer_trusted.
- verifing Glue job is successful and only contains Customer Records from people who agreed to share their data. Query your Glue customer_trusted table with Athena and take a screenshot of the data. Name the screenshot customer_trusted(.png,.jpeg, etc.).

Data Scientists have discovered a data quality issue with the Customer Data. The serial number should be a unique identifier for the STEDI Step Trainer they purchased. However, there was a defect in the fulfillment website, and it used the same 30 serial numbers over and over again for millions of customers! Most customers have not received their Step Trainers yet, but those who have, are submitting Step Trainer data over the IoT network (Landing Zone). The data from the Step Trainer Records has the correct serial numbers.

The problem is that because of this serial number bug in the fulfillment data (Landing Zone), we don’t know which customer the Step Trainer Records data belongs to.

The Data Science team would like to write a Glue job:

- Read the Step Trainer IoT data stream (S3) and populate a Trusted Zone Glue Table called step_trainer_trusted that contains the Step Trainer Records data for customers who have accelerometer data and have agreed to share their data for research (customers_curated).
- Create an aggregated table that has each of the Step Trainer Readings, and the associated accelerometer reading data for the same timestamp, but only for customers who have agreed to share their data, and make a glue table called machine_learning_curated.




