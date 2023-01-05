---
title : "Khởi tạo EC2 instance"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 2.2 </b> "
---

#### Khởi tạo EC2 instance

1.  Truy cập [AWS Management Console](https://aws.amazon.com/console/)

- Tìm **EC2**
- Chọn **EC2**

![CreateEC2instance](/images/2/0001.png?featherlight=false&width=90pc)

2. Trong giao diện **EC2**

- Chọn **Instances**
- Chọn **Launch instances**

![CreateEC2instance](/images/2/0002.png?featherlight=false&width=90pc)

3. Trong giao diện **Launch instances**

- **Name and tags**, nhập ```CloudWatch-instance```

![CreateEC2instance](/images/2/0003.png?featherlight=false&width=90pc)

4. Trong giao diện **Launch instances**

- Chọn **Quick Start**
- Chọn **Amazon Linux**
- Chọn loại **AMI**

![CreateEC2instance](/images/2/0004.png?featherlight=false&width=90pc)

5. Tiếp tục trong giao diện **Launch instances**

- Chọn **Instance type**
- Chọn **Create new key pair**

![CreateEC2instance](/images/2/0005.png?featherlight=false&width=90pc)

6. Trong giao diện **Create key pair**

- **Key pair name**, nhập ```CloudWatchKey```
- **Key pair type**, chọn **RSA**
- **Private key file format**, chọn **.pem**
- Chọn **Create key pair**
- Lưu trữ key pair để thực hiện kết nối EC instance ở các bước sau

![CreateEC2instance](/images/2/0006.png?featherlight=false&width=90pc)

7. Trong giao diện **Launch instances**

- Trong phần **Network settings**, chọn **Edit**

![CreateEC2instance](/images/2/0007.png?featherlight=false&width=90pc)

8. Trong giao diện **Network settings**

- **VPC**, chọn VPC vừa tạo
- **Subnet**, chọn **Public subnet** đã được enable auto-assign IPv4 address
- **Auto-assign public IP**, chọn **Enable**
- **Firewall (security group)**, Chọn **Select existing security group**
- Chọn **Security group** vừa tạo

![CreateEC2instance](/images/2/0008.png?featherlight=false&width=90pc)

9. Kiểm tra lại và chọn **Launch instances**

![CreateEC2instance](/images/2/0009.png?featherlight=false&width=90pc)

10. Chọn **View all instances**

![CreateEC2instance](/images/2/00010.png?featherlight=false&width=90pc)

11. Xem thông tin chi tiết instance vừa tạo

![CreateEC2instance](/images/2/00011.png?featherlight=false&width=90pc)

