---
title : "Create VPC and Security Group"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 2.1 </b> "
---

#### Prepare VPC, Security Group for EC2 instance

1. Access the interface [AWS Management Console](https://aws.amazon.com/console/)

- Find **VPC**
- Select **VPC**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/0001-createec2instance.png)

2. In the **VPC** interface

- Select **Your VPCs**
- Select **Create VPC**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/0002-createec2instance.png)

3. In the **Create VPC** interface

- In **VPC settings**, select **VPC, subents, etc.**
- **Name tag auto-generation**, enter ```cloudwatch```
- **IPv4 CIDR block**, enter ```10.0.0.0/16```
- **IPv6 CIDR block**, select **No IPv6 CIDR block**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/0003-createec2instance.png)

4. Select **Create VPC**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/0004-createec2instance.png)

5. Select **View VPC**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/0005-createec2instance.png)

6. Complete VPC . Creation

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/0006-createec2instance.png)

7. In the **VPC** interface

- Select **Subnets**
- Select **Public subnet**
- Check **Auto-assign public IPv4 address**
- Then select **Actions**
- Select **Edit subnet settings**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/0007-createec2instance.png)

8. In the **Edit subnet settings** interface

- Step **Auto-assign IP settings**, select *Enable auto-assign public IPv4 address**
- Select **Save**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/0008-createec2instance.png)

9. **Enable auto-assign public IPv4 address** successfully

- Check **Auto-assign public IPv4 address**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/0009-createec2instance.png)

10. Go to the [AWS Management Console](https://aws.amazon.com/console/)

- Find **VPC**
- Select **VPC**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/0001-createec2instance.png)

11. In the **VPC** interface

- Select **Security Group**
- Select **Create security group**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00010-createec2instance.png)

12. In the **Create security group** interface

- **Security group name**, enter ```cloudwatch-subnet```
- **Description**, enter ```Subnet for CloudWatch instance```
- **VPC**, select the newly created VPC

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00011-createec2instance.png)

13. Configure **Inbound rules**

- Select **Add rule** and proceed with configuration
- **SSH**
- **All ICMP-IPv4**
- **All ICMP-IPv6**
- **HTTP**
- **HTTPS**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00012-createec2instance.png)

14. Select *Create security group**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00013-createec2instance.png)

15. Complete initialization **Security group**

![CreateEC2instance](/images/2-Prerequiste/2.1-Createec2instance/00014-createec2instance.png)
