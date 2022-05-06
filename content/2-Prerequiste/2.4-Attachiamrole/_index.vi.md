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

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0001-attachiamrole.png)

2. Trong giao diện **EC2**

- Chọn **Instances**
- Chọn instance vừa tạo 

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0002-attachiamrole.png)

3. Trong giao diện **EC2**

- Chọn **Actions**
- Chọn **Security**
- Chọn **Modify IAM role**

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0003-attachiamrole.png)

4. Trong giao diện **Modify IAM role**

- Chọn **CloudWatchAgentRole**
- Chọn **Save**

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0004-attachiamrole.png)

5. Hoàn thành gán role thành công

- Kiểm tra instance đã được gán IAM role

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0005-attachiamrole.png)

