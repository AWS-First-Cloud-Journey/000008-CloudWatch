---
title : "Tạo IAM role"
date :  "`r Sys.Date()`" 
weight : 3 
chapter : false
pre : " <b> 2.3 </b> "
---

#### Tạo IAM role
Trong phần này, bạn sẽ thực hành cài đặt CloudWatch Agent để theo dõi RAM của EC2 Instance và gửi dữ liệu về cho CloudWatch. Để EC2 Instance có quyền truy cập vào CloudWatch, bạn cần gán cho nó một IAM Role phù hợp.

1. Truy cập [AWS Management Console](https://aws.amazon.com/console/)

- Tìm **IAM**
- Chọn **IAM**

![CreateIAMrole](/images/3/0001.png?featherlight=false&width=90pc)

2. Trong giao diện **IAM**

- Chọn **Roles**
- Chọn **Create role**

![CreateIAMrole](/images/3/0002.png?featherlight=false&width=90pc)

3. Trong giao diện **Select trusted entity**

- Chọn **AWS service**
- **Use case**, chọn **EC2**

![CreateIAMrole](/images/3/0003.png?featherlight=false&width=90pc)

4. Trong giao diện **Add permissions**

- Tìm kiếm **CloudWatchAgentServer** policy
- Chọn **CloudWatchAgentServer** policy
- Chọn **Next**

![CreateIAMrole](/images/3/0004.png?featherlight=false&width=90pc)

5. Trong phần **Role details**

- Chọn **CloudWatchAgentRole**

![CreateIAMrole](/images/3/0005.png?featherlight=false&width=90pc)

6. Chọn **Create role**

![CreateIAMrole](/images/3/0006.png?featherlight=false&width=90pc)

7. Hoàn thành tạo role

![CreateIAMrole](/images/3/0007.png?featherlight=false&width=90pc)