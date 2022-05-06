---
title : "Create EC2 instance"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---


1. Go to the [AWS Management Console](https://aws.amazon.com/console/)

- Find **EC2**
- Select **EC2**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00015-createec2instance.png)

2. In the **EC2** interface

- Select **Instances**
- Select **Launch instances**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00016-createec2instance.png)

3. In the **Launch instances** interface

- **Name and tags**, enter ```CloudWatch-instance```

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00017-createec2instance.png)

4. In the **Launch instances** interface

- Select **Quick Start**
- Select **Amazon Linux**
- Select type **AMI**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00018-createec2instance.png)

5. Continue in **Launch instances** interface

- Select **Instance type**
- Select **Create new key pair**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00019-createec2instance.png)

6. In the **Create key pair** interface

- **Key pair name**, enter ```CloudWatchKey```
- **Key pair type**, select **RSA**
- **Private key file format**, select **.pem**
- Select **Create key pair**
- Store the key pair to make EC instance connection in the following steps

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00020-createec2instance.png)

7. In the **Launch instances** interface

- In the **Network settings** section, select **Edit**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00021-createec2instance.png)

8. In the **Network settings** interface

- **VPC**, select the newly created VPC
- **Subnet**, select **Public subnet** already enabled auto-assign IPv4 address
- **Auto-assign public IP**, select **Enable**
- **Firewall (security group)**, Select **Select existing security group**
- Select **Security group** just created

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00022-createec2instance.png)

9. Double check and select **Launch instances**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00023-createec2instance.png)

10. Select **View all instances**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00024-createec2instance.png)

11. View the details of the newly created instance

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00025-createec2instance.png)