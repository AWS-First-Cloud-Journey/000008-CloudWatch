---
title : "Launch EC2 instance"
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

#### Launch EC2 instance

1. Go to [AWS Management Console](https://aws.amazon.com/console/)

- Find **EC2**
- Select **EC2**

![CreateEC2instance](/images/2/0001.png?featherlight=false&width=90pc)

2. In the **EC2** interface

- Select **Instances**
- Select **Launch instances**

![CreateEC2instance](/images/2/0002.png?featherlight=false&width=90pc)

3. In the **Launch instances** interface

- **Name and tags**, enter ```CloudWatch-instance```

![CreateEC2instance](/images/2/0003.png?featherlight=false&width=90pc)

4. In the **Launch instances** interface

- Select **Quick Start**
- Select **Amazon Linux**
- Select type **AMI**

![CreateEC2instance](/images/2/0004.png?featherlight=false&width=90pc)

5. Continue in **Launch instances** interface

- Select **Instance type**
- Select **Create new key pair**

![CreateEC2instance](/images/2/0005.png?featherlight=false&width=90pc)

6. In the **Create key pair** interface

- **Key pair name**, enter ```CloudWatchKey```
- **Key pair type**, select **RSA**
- **Private key file format**, select **.pem**
- Select **Create key pair**
- Store the key pair to make EC instance connection in the following steps

![CreateEC2instance](/images/2/0006.png?featherlight=false&width=90pc)

7. In the **Launch instances** interface

- In the **Network settings** section, select **Edit**

![CreateEC2instance](/images/2/0007.png?featherlight=false&width=90pc)

8. In the **Network settings** interface

- **VPC**, select the newly created VPC
- **Subnet**, select **Public subnet** already enabled auto-assign IPv4 address
- **Auto-assign public IP**, select **Enable**
- **Firewall (security group)**, Select **Select existing security group**
- Select **Security group** just created

![CreateEC2instance](/images/2/0008.png?featherlight=false&width=90pc)

9. Double check and select **Launch instances**

![CreateEC2instance](/images/2/0009.png?featherlight=false&width=90pc)

10. Select **View all instances**

![CreateEC2instance](/images/2/00010.png?featherlight=false&width=90pc)

11. View the details of the newly created instance

![CreateEC2instance](/images/2/00011.png?featherlight=false&width=90pc)