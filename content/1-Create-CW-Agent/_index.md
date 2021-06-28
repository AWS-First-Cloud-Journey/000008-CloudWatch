+++
title = "CloudWatch Agent"
date = 2020-04-18T00:38:32+07:00
weight = 1
chapter = false
pre = "<b>1. </b>"
+++
#### Tổng quan

Trong phần này, bạn sẽ thực hành cài đặt CloudWatch Agent để theo dõi RAM của EC2 Instance và gửi dữ liệu về cho CloudWatch. Để EC2 Instance có quyền truy cập vào CloudWatch, bạn cần gán cho nó một IAM Role phù hợp.

![Architecture](/images/5-monitoring/000008Architect.png?width=40pc)

#### Nội dung:
- [1.1. Khởi tạo IAM Role](1-create-iam-role/)
- [1.2. Gán IAM Role vào Instance](2-attach-iam-role/)
- [1.3. Cài đặt CloudWatch Agent](3-install-cw-agent/)