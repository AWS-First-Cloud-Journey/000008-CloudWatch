+++
title = "Khởi tạo IAM Role"
date = 2020-04-18T00:38:32+07:00
weight = 2
chapter = false
pre = "<b>2.2. </b>"
+++

**Nội dung:**
- [Khởi tạo IAM Role](#khởi-tạo-iam-role)

#### Khởi tạo IAM Role

+ Bạn cần khởi tạo IAM Role để có thể cấp quyền cho EC2 Instance gửi thông tin lên AWS CloudWatch


1. Vào trang quản trị [**IAM Console**](https://console.aws.amazon.com/iam/home).
2. Tại khung tính năng, chọn **Roles** và chọn **Create role**.

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-6.PNG?width=90pc)

3. Tại **Create role**, chọn use case **EC2** và chọn **Next Permission**.  

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-7.PNG?width=90pc)

4. Chọn **Policy** tên là **CloudWatchAgentServerPolicy**.

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-8.PNG?width=90pc)

5. Điền tags: Key and Value.
6. Điền Role Information **Role name**, **Role description** và chọn **Create role**

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-9.PNG?width=90pc)
