---
title : "Các bước chuẩn bị"
date :  "`r Sys.Date()`" 
weight : 2 
chapter : false
pre : " <b> 2. </b> "
---

#### Tổng quan

Trong phần này, bạn sẽ thực hành cài đặt CloudWatch Agent để theo dõi RAM của EC2 Instance và gửi dữ liệu về cho CloudWatch. Để EC2 Instance có quyền truy cập vào CloudWatch, bạn cần gán cho nó một IAM Role phù hợp.

#### Nội dung

1. [Tạo VPC và Security Group](2.1-createvpcandsecuritygroup)
2. [Khởi tạo EC2 instance](2.2-createec2instance)
3. [Tạo IAM Role](2.3-createiamrole)
4. [Gán IAM Role vào EC2 instance](2.4-attachiamrole)