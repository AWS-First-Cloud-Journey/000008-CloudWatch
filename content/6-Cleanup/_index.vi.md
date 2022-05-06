---
title : "Dọn dẹp tài nguyên"
date :  "`r Sys.Date()`" 
weight : 6
chapter : false
pre : " <b> 6. </b> "
---

Chúng ta sẽ dọn dẹp tài nguyên theo thứ tự như sau:

#### Xóa Dashboard

1. Truy cập [CloudWatch Management Console](https://aws.amazon.com/console/)
2. Trên thanh điều hướng bên trái, chọn **Dashboards**
3. Chọn tất cả **CloudWatch Dasboards** liên quan tới bài lab.  
4. Click **Delete**
5. Trong prompt, click **Delete**


#### Xóa IAM Role

1. Truy cập [IAM Management Console](https://aws.amazon.com/console/)
2. Trên thanh điều hướng bên trái, chọn **Roles**
3. Trong hộp tìm kiếm, tìm và chọn tất cả Roles liên quan tới bài lab.
4. Click **Delete Role**
5. Trong prompt, click **Yes**, **Delete**

#### Terminate EC2 instance

1. Truy cập [EC2 Management Console](https://aws.amazon.com/console/)
2. Trên thanh điều hướng bên trái, chọn **Intances**
3. Chọn tất cả **EC2 Instance** liên quan tới bài lab.
4. Click **Actions**.
5. Click **Manage Instance State**.
6. Chọn **Terminate**.
7. Click **Change State**