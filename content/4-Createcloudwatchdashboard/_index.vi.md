---
title : "Tạo CloudWatch Dashboard"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 4. </b> "
---

#### Tạo CloudWatch Dashboard

Để bắt đầu với CloudWatch Dashboard, trước tiên bạn cần tạo 1 dashboard mới. Bạn có thể tạo nhiều dashboard. Không có giới hạn về số lượng dashboard trong 1 tài khoản AWS. Tất cả các dashboard là Global, không nằm riêng trong 1 vùng region nào cả


1. Truy cập giao diện [AWS Management Console](https://aws.amazon.com/console/)

- Tìm **CloudWatch**
- Chọn **CloudWatch**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0001-createcloudwatchdashboard.png)

2. Trong giao diện **CloudWatch**

- Chọn **Dashboard**
- Chọn **Custom dashboard**
- Chọn **Create dashboard**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0002-createcloudwatchdashboard.png)

3. Trong giao diện **Create new dashboard**

- **Dashboard name**, nhập ```MyFirstDashboard```
- Chọn **Create dashboard**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0003-createcloudwatchdashboard.png)

4. Tại prompt **Add Widget**, chọn loại giao diện **Line**. Trong giao diện **Add to this dashboard**

- Chọn **Metrics**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0004-createcloudwatchdashboard.png)

5. Trong giao diện **Add metric graph**

- Chọn **Browse**
- **Custom namespaces**, chọn **CWAgent**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0005-createcloudwatchdashboard.png)

6. Tiếp theo, chọn **host**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0006-createcloudwatchdashboard.png)

7. Chọn host theo **Hostname type** của instance vừa tạo

- Chọn **Create widget**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0007-createcloudwatchdashboard.png)

8. Hoàn thành tạo dashboard CloudWatch

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0008-createcloudwatchdashboard.png)

9. Phóng to dashboard để xem dễ dàng và chọn **View in metrics**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0009-createcloudwatchdashboard.png)

10. Trong giao diện **CloudWatch metrics**

- Quan sát giao diện và các tính năng

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00010-createcloudwatchdashboard.png)

11. Trong giao diện **CloudWatch metrics**

- Chọn **Add query**
- Chọn **EC2**
- Chọn **Average Active CPU for an application (CloudWatch Agent)**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00011-createcloudwatchdashboard.png)

12. Kết quả query được hiển thị

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00012-createcloudwatchdashboard.png)

13. Tiếp tục, trong giao diện **CloudWatch metrics**

- Chọn **Add math**
- Chọn **Search**
- Chọn **EC2 CPU utilization**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00013-createcloudwatchdashboard.png)

14. Kết quả hiện thị, chọn **CWgent hostname type** của instance và quan sát biểu đồ

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00014-createcloudwatchdashboard.png)

15. Quay trở lại giao diện **CloudWatch Dashboard**

- Chọn **Save dashboard**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00015-createcloudwatchdashboard.png)
