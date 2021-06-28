+++
title = "Tạo CloudWatch Dashboard"
date = 2020-04-18T00:38:32+07:00
weight = 2
chapter = false
pre = "<b>2. </b>"
+++

Ở phần này, bạn sẽ thực hành tạo CloudWatch Dasboard để thể hiện dữ liệu vừa thu thập được từ CloudWatch Agent ở EC2 Instance bạn tạo ở phần 1.

**Nội dung:**
- [Khởi tạo AWS CloudWatch Dashboard](#khởi-tạo-aws-cloudwatch-dashboard)

#### Khởi tạo AWS CloudWatch Dashboard

Để bắt đầu với CloudWatch Dashboard, trước tiên bạn cần tạo 1 dashboard mới. Bạn có thể tạo nhiều dashboard. Không có giới hạn về số lượng dashboard trong 1 tài khoản AWS. Tất cả các dashboard là Global, không nằm riêng trong 1 vùng region nào cả

1. Đăng nhập vào trang quản trị AWS Management Console và vào dịch vụ AWS CloudWatch tại [**CloudWatch console**](https://console.aws.amazon.com/cloudwatch/home).
2. Chọn **Dashboards** ở thanh bên trái và Chọn **Create dashboard**.
![Create CloudWatch Dashboard](/images/5-monitoring/2_CreateDashboard.png?width=90pc)
3. Tại prompt **Create new dashboard**, đặt tên cho dashboard và chọn **Create dashboard**.  
4. Tại prompt **Add Widget**, chọn loại giao diện **Line**.
![Create CloudWatch Dashboard](/images/5-monitoring/2_WidgetType.png?width=90pc)
5. Chọn nguồn cung cấp dữ liệu **Metrics** và chọn **Configure**.
6. Trong bảng **Add metric graph**, chọn dịch vụ **CWAgent**
![Create CloudWatch Dashboard](/images/5-monitoring/2_PickCWAgent.png?width=90pc)
7. Chọn **host**, tick vào EC2 Instance mà bạn đã tạo cho bài lab này, và chọn **Create widget**.
![Create CloudWatch Dashboard](/images/5-monitoring/2_PickMetrics.png?width=90pc)
{{% notice note %}}
Tên của EC2 Instance được thể hiện ở trong CloudWatch là sự kết hợp của Private IP và Region của EC2 Instance đó. Cụ thể ở hình trên, EC2 Instance có private IP là 172.31.37.188 và nằm ở region ap-southeast-1, tức Singapore.
{{% /notice %}}

8. Chọn **Save dashboard** để lưu lại Dashboard.
![Create CloudWatch Dashboard](/images/5-monitoring/2_SaveDashboard.png?width=90pc)
