+++
title = "Gán IAM Role vào Instance"
date = 2020-04-18T00:38:32+07:00
weight = 2
chapter = false
pre = "<b>1.2. </b>"
+++
Ở bước này, bạn sẽ gán IAM Role vừa được tạo vào EC2 Instance.

**Nội dung:**
- [Gán IAM Role vào Instance](#gán-iam-role-vào-instance)
- [Kiếm tra dữ liệu được gửi về CloudWatch](#kiếm-tra-dữ-liệu-được-gửi-về-cloudwatch)
#### Gán IAM Role vào Instance

1. Vào trang quản trị [**EC2 Instance Console**](https://console.aws.amazon.com/ec2).
2. Tại thanh bên trái, chọn **Instances**,
3. Tiến hành khởi tạo EC2 Instance sử dụng **Amazon Linux 2 AMI (HVM)**.
{{% notice note %}}
Nếu bạn chưa biết cách khởi tạo EC2 Instance, mời bạn tham khảo bài [Sử dụng Máy ảo Linux](https://000004.awsstudygroup.com/vi/0-getting-started-ec2/1-create-ec2-instance/3-working-with-linux-instance/)
{{% /notice %}}
4. Chọn EC2 Instance vừa được tạo, và chọn **Action** -> **Security** -> **Modify IAM Role**.
![Install CloudWatch Agent](/images/5-monitoring/1.2_ModifyIAM.png?width=90pc)
5. Chọn IAM Role mà bạn vừa tạo, và chọn **Save**.  
![Install CloudWatch Agent](/images/5-monitoring/1.2_Save.png?width=90pc)

