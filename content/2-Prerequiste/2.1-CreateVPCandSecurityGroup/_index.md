---
title : "Create VPC and Security Group"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 2.1 </b> "
---

#### Prepare VPC, Security Group for EC2 instance

1. Access the [AWS Management Console](https://aws.amazon.com/console/)

   - Find **VPC**
   - Select **VPC**

![CreateEC2instance](/images/1/0001.png?featherlight=false&width=90pc)

2. In the **VPC** interface

   - Select **Your VPCs**
   - Select **Create VPC**

![CreateEC2instance](/images/1/0002.png?featherlight=false&width=90pc)

3. In the **Create VPC** interface

    - In **VPC settings**, select **VPC, subnets, etc.**
    - **Name tag auto-generation**, enter ```cloudwatch```
    - **IPv4 CIDR block**, enter ```10.0.0.0/16```
    - **IPv6 CIDR block**, select **No IPv6 CIDR block**

![CreateEC2instance](/images/1/0003.png?featherlight=false&width=90pc)

4. Select **Create VPC**

![CreateEC2instance](/images/1/0004.png?featherlight=false&width=90pc)

5. Select **View VPC**

![CreateEC2instance](/images/1/0005.png?featherlight=false&width=90pc)

6. Complete VPC creation.

![CreateEC2instance](/images/1/0006.png?featherlight=false&width=90pc)

7. In the **VPC** interface

   - Select **Subnets**
   - Select **Public subnet**
   - Check **Auto-assign public IPv4 address**
   - Then select **Actions**
   - Select **Edit subnet settings**

![CreateEC2instance](/images/1/0007.png?featherlight=false&width=90pc)

8. In the **Edit subnet settings** interface

   - Step **Auto-assign IP settings**, select *Enable auto-assign public IPv4 address**
   - Select **Save**

![CreateEC2instance](/images/1/0008.png?featherlight=false&width=90pc)

9. **Enable auto-assign public IPv4 address** successfully

   - Check **Auto-assign public IPv4 address**

![CreateEC2instance](/images/1/0009.png?featherlight=false&width=90pc)

10. Go to the [AWS Management Console](https://aws.amazon.com/console/)

    - Find **VPC**
    - Select **VPC**

![CreateEC2instance](/images/1/00010.png?featherlight=false&width=90pc)

11. In the **VPC** interface

    - Select **Security Group**
    - Select **Create security group**

![CreateEC2instance](/images/1/00011.png?featherlight=false&width=90pc)

12. In the **Create security group** interface

    - **Security group name**, enter ```cloudwatch-subnet```
    - **Description**, enter ```Subnet for CloudWatch instance```
    - **VPC**, select the newly created VPC

![CreateEC2instance](/images/1/00012.png?featherlight=false&width=90pc)

13. Configure **Inbound rules**

    - Select **Add rule** and proceed with configuration
    - **SSH**
    - **All ICMP-IPv4**
    - **All ICMP-IPv6**
    - **HTTP**
    - **HTTPS**

![CreateEC2instance](/images/1/00013.png?featherlight=false&width=90pc)

14. Select *Create security group**

![CreateEC2instance](/images/1/00014.png?featherlight=false&width=90pc)

15. Complete initialization **Security group**