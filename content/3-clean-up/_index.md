+++
title = "Dọn Dẹp Tài Nguyên"
date = 2021-06-10T22:28:55+07:00
weight = 3
chapter = false
pre = "<b>3. </b>"
+++

Chúng ta sẽ dọn dẹp tài nguyên theo thứ tự như sau:

1.  Xóa Dashboard
    - Truy cập **CloudWatch Management Console**
    - Trên thanh điều hướng bên trái, chọn Dashboards
    - Chọn tất cả CloudWatch Dasboards liên quan tới bài lab.
    - Click Delete
    - Trong prompt, click Delete
    
2. Xóa IAM Role
    - Truy cập **IAM Management Console**
    - Trên thanh điều hướng bên trái, chọn Roles
    - Trong hộp tìm kiếm, tìm và chọn tất cả Roles liên quan tới bài lab.
    - Click Delete Role
    - Trong prompt, click Yes, Delete
![Delete Role](/images/5-monitoring/3_DeleteRole.png?width=90pc)

3. **Terminate EC2 instance**
    - Truy cập **EC2 Management Console** 
    - Trên thanh điều hướng bên trái, chọn Intances
    - Chọn tất cả EC2 Instance liên quan tới bài lab.
    - Click Actions.
    - Click Manage Instance State.
    - Chọn Terminate.
    - Click Change State