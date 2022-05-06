---
title : "Giới thiệu"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

#### Amazon CloudWatch
Amazon CloudWatch là một công cụ cho phép bạn thu thập dữ liệu về hoạt động của các tài nguyên, ứng dụng, và dịch vụ đang vận hành trên AWS Cloud hoặc máy chủ của bạn. Dữ liệu thu thập được sẽ được lưu dưới dạng các nhật ký, chỉ số, và sự kiện. Cloudwatch cũng có thể thể hiện dữ liệu dưới dạng biểu đồ để bạn dễ dàng hình dung và chắt lọc thông tin từ dữ liệu.

#### CloudWatch Agent
CloudWatch Agent là một ứng dụng thuộc dịch vụ CloudWatch. Bạn cần tải về và khởi chạy CloudWatch Agent trên máy chủ on-premise hoặc EC2 Instance để CloudWatch có thể thu thập dữ liệu hoạt động của từng máy.

Trong phần này, bạn sẽ thực hành cài đặt CloudWatch Agent để theo dõi RAM của EC2 Instance và gửi dữ liệu về cho CloudWatch. Để EC2 Instance có quyền truy cập vào CloudWatch, bạn cần gán cho nó một IAM Role phù hợp.

![CloudWatch](/images/architect.png)