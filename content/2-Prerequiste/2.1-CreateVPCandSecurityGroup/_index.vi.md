---
title : "Tạo VPC và Security Group"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 2.1 </b> "
---

#### Chuẩn bị VPC, Security Group cho EC2 instance

1. Truy cập giao diện [AWS Management Console](https://aws.amazon.com/console/)

   - Tìm **VPC**
   - Chọn **VPC**

![CreateEC2instance](/images/1/0001.png?featherlight=false&width=90pc)

2. Trong giao diện **VPC**

   - Chọn **Your VPCs**
   - Chọn **Create VPC**

![CreateEC2instance](/images/1/0002.png?featherlight=false&width=90pc)

3. Trong giao diện **Create VPC**

    - Trong **VPC settings**, chọn **VPC, subents, etc.**
    - **Name tag auto-generation**, nhập ```cloudwatch```
    - **IPv4 CIDR block**, nhập ```10.0.0.0/16```
    - **IPv6 CIDR block**, chọn **No IPv6 CIDR block**

![CreateEC2instance](/images/1/0003.png?featherlight=false&width=90pc)

4. Chọn **Create VPC**

![CreateEC2instance](/images/1/0004.png?featherlight=false&width=90pc)

5. Chọn **View VPC**

![CreateEC2instance](/images/1/0005.png?featherlight=false&width=90pc)

6. Hoàn thành tạo VPC

![CreateEC2instance](/images/1/0006.png?featherlight=false&width=90pc)

7. Trong giao diện **VPC**

   - Chọn **Subnets**
   - Chọn **Public subnet**
   - Kiểm tra **Auto-assign public IPv4 address**
   - Sau đó chọn **Actions**
   - Chọn **Edit subnet settings**

![CreateEC2instance](/images/1/0007.png?featherlight=false&width=90pc)

8. Trong giao diện **Edit subnet settings**

   - Bước **Auto-assign IP settings**, chọn *Enable auto-assign public IPv4 address**
   - Chọn **Save**

![CreateEC2instance](/images/1/0008.png?featherlight=false&width=90pc)

9. **Enable auto-assign public IPv4 address** thành công

   - Kiểm tra **Auto-assign public IPv4 address**

![CreateEC2instance](/images/1/0009.png?featherlight=false&width=90pc)

10.  Truy cập [AWS Management Console](https://aws.amazon.com/console/)

    - Tìm **VPC**
    - Chọn **VPC**

![CreateEC2instance](/images/1/00010.png?featherlight=false&width=90pc)

11.  Trong giao diện **VPC**

    - Chọn **Security Group**
    - Chọn **Create security group**

![CreateEC2instance](/images/1/00011.png?featherlight=false&width=90pc)

12.  Trong giao diện **Create security group**

    - **Security group name**, nhập ```cloudwatch-subnet```
    - **Description**, nhập ```Subnet for CloudWatch instance```
    - **VPC**, chọn VPC vừa tạo

![CreateEC2instance](/images/1/00012.png?featherlight=false&width=90pc)

13.  Thực hiện cấu hình **Inbound rules**

    - Chọn **Add rule** và tiến hành cấu hình
    - **SSH**
    - **All ICMP-IPv4**
    - **All ICMP-IPv6**
    - **HTTP**
    - **HTTPS**

![CreateEC2instance](/images/1/00013.png?featherlight=false&width=90pc)

14.  Chọn *Create security group**

![CreateEC2instance](/images/1/00014.png?featherlight=false&width=90pc)

15. Hoàn thành khởi tạo **Security group**

