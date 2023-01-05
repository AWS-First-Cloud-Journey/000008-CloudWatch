---
title : "Gán IAM role"
date :  "`r Sys.Date()`" 
weight : 4 
chapter : false
pre : " <b> 2.4 </b> "
---

#### Gán IAM role
1. Truy cập [AWS Management Console](https://aws.amazon.com/console/)

- Tìm **EC2**
- Chọn **EC2**

![Attach IAM Role](/images/4/0001.png?featherlight=false&width=90pc)

1. Trong giao diện **EC2**

- Chọn **Instances**
- Chọn instance vừa tạo 

![Attach IAM Role](/images/4/0002.png?featherlight=false&width=90pc)

3. Trong giao diện **EC2**

- Chọn **Actions**
- Chọn **Security**
- Chọn **Modify IAM role**

![Attach IAM Role](/images/4/0003.png?featherlight=false&width=90pc)

4. Trong giao diện **Modify IAM role**

- Chọn **CloudWatchAgentRole**
- Chọn **Save**

![Attach IAM Role](/images/4/0004.png?featherlight=false&width=90pc)

5. Hoàn thành gán role thành công

- Kiểm tra instance đã được gán IAM role

![Attach IAM Role](/images/4/0005.png?featherlight=false&width=90pc)

