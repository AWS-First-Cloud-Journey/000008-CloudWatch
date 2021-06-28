+++
title = "Khởi tạo IAM Role"
date = 2020-04-18T00:38:32+07:00
weight = 1
chapter = false
pre = "<b>1.1. </b>"
+++

Ở bước này, bạn sẽ khởi tạo IAM Role để cho phép EC2 Instance có quyền truy cập vào CloudWatch trong tài khoản của bạn.

**Nội dung:**
- [Khởi tạo IAM Role](#khởi-tạo-iam-role)

#### Khởi tạo IAM Role

1. Vào trang [**IAM Management Console**](https://console.aws.amazon.com/iam/home).
2. Tại thanh bên trái, chọn **Roles** và chọn **Create role**.
![Install CloudWatch Agent](/images/5-monitoring/1.1_CreateIAM.png?width=90pc)
3. Tại trang **Create role**, chọn **AWS service**, chọn use case **EC2**, rồi chọn **Next Permission**.  
![Install CloudWatch Agent](/images/5-monitoring/1.1_EC2UseCase.png?width=90pc)
4. Chọn **Policy** tên là **CloudWatchAgentServerPolicy** và chọn **Next: Tags**
![Install CloudWatch Agent](/images/5-monitoring/1.1_CWPolicy.png?width=90pc)
5. Chọn **Next: Review**
6. Điền Role Information **Role name**, **Role description** và chọn **Create role**. Hãy nhớ **RoleName** của mình để sử dụng trong bước tiếp theo
![Install CloudWatch Agent](/images/5-monitoring/1.1_Review.png?width=90pc)
