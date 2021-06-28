+++
title = "Quản lý tài nguyên với Cloud Watch"
date = 2020-04-18T00:38:32+07:00
weight = 1
chapter = false
+++

# Quản lý tài nguyên với Cloud Watch

#### Tổng quan

Ở bài lab này, bạn sẽ thiết lập **CloudWatch Agent** trên EC2 Instance để thu thập dữ liệu hoạt động của instance và gửi về cho **CloudWatch**. Sau đó, bạn sẽ thể hiện dữ liệu thu thập được lên CloudWatch Dashboard.

#### AWS CloudWatch
**AWS CloudWatch** là một công cụ cho phép bạn thu thập dữ liệu về hoạt động của các tài nguyên, ứng dụng, và dịch vụ đang vận hành trên AWS Cloud hoặc máy chủ của bạn. Dữ liệu thu thập được sẽ được lưu dưới dạng các nhật ký, chỉ số, và sự kiện. Cloudwatch cũng có thể thể hiện dữ liệu dưới dạng biểu đồ để bạn dễ dàng hình dung và chắt lọc thông tin từ dữ liệu.

#### CloudWatch Agent
**CloudWatch Agent** là một ứng dụng thuộc dịch vụ CloudWatch. Bạn cần tải về và khởi chạy CloudWatch Agent trên máy chủ on-premise hoặc EC2 Instance để CloudWatch có thể thu thập dữ liệu hoạt động của từng máy.


#### Nội dung:
1. [CloudWatch Agent](1-create-cw-agent)
2. [Tạo CloudWatch Dashboard](2-create-aws-dashboard)
3. [Dọn Dẹp Tài Nguyên](3-clean-up)