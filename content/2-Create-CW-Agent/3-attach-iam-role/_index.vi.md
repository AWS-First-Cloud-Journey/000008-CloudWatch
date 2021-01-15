+++
title = "Gán IAM Role"
date = 2020-04-18T00:38:32+07:00
weight = 3
chapter = false
pre = "<b>2.3. </b>"
+++

**Nội dung:**
- [Gán IAM Role vào Instance](#gán-iam-role-vào-instance)

#### Gán IAM Role vào Instance

1. Vào trang quản trị [**EC2 Instance Console**](https://console.aws.amazon.com/ec2).
2. Tại khung tính năng, chọn **Instances**, chọn Instance mà bạn muốn gán IAM Role, và chọn **Action** -> **Instance Setting** -> **Attach/Replace IAM Role**.

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-10.PNG?width=90pc)

3. Chọn IAM Role mà bạn vừa tạo, và chọn **Apply**.  

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-11.PNG?width=90pc)

4. Vào trang quản trị [**CloudWatch Console**](https://console.aws.amazon.com/cloudwatch/home)
5. Tại khung tính năng, chọn **Metrics**.
6. Sau vài giây, bạn có thể thấy được **custom metric** xuất hiện, Vào trong đó bạn có thể thấy được memory metric đã được gửi tới CloudWatch  

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-13.PNG?width=90pc)

