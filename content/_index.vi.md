---
title: "AWS CloudWatch Workshop"
weight: 1
chapter: false
---

# AWS CloudWatch Workshop

![architecture](/images/architecture.png)

#### Tổng quan

**ℹ️ Information**: **Amazon CloudWatch** là dịch vụ theo dõi và quản lý cung cấp dữ liệu và thông tin định hướng hành động cho tài nguyên cơ sở hạ tầng và ứng dụng AWS, ứng dụng hybrid cũng như ứng dụng on-premises. Bạn có thể thu thập và truy cập tất cả dữ liệu về hiệu năng và hoạt động dưới hình thức logs và metrics trong cùng một nền tảng, thay vì theo dõi riêng lẻ (máy chủ, mạng hoặc cơ sở dữ liệu). **CloudWatch** cho phép bạn theo dõi end-to-end (ứng dụng, cơ sở hạ tầng và dịch vụ) và tận dụng cảnh báo, logs và dữ liệu sự kiện để tự động hóa các hành động và giảm Mean Time To Resolution (MTTR). Dịch vụ này giúp bạn giải phóng tài nguyên quan trọng và tập trung vào việc xây dựng các ứng dụng và giá trị kinh doanh.

#### Tính năng chính

**CloudWatch** cung cấp thông tin định hướng hành động, hỗ trợ việc tối ưu hóa hiệu năng ứng dụng, quản lý sử dụng tài nguyên và hiểu rõ tình trạng hoạt động của toàn hệ thống. **CloudWatch** hiển thị dữ liệu metrics và logs chi tiết đến từng giây, lưu trữ dữ liệu trong 15 tháng (đối với metrics) và cho phép thực hiện các phép tính trên metrics. 

**💡 Pro Tip**: Dịch vụ này cũng giúp bạn phân tích dựa trên dữ liệu lịch sử nhằm tối ưu hóa chi phí và thu thập thông tin real-time để tối ưu hóa ứng dụng và tài nguyên cơ sở hạ tầng.

#### Container Insights

**ℹ️ Information**: **CloudWatch Container Insights** cho phép bạn theo dõi, khắc phục sự cố và thiết lập cảnh báo cho các ứng dụng và microservices chạy trong containers. **CloudWatch** thu thập, tổng hợp và tóm tắt thông tin sử dụng tài nguyên tính toán (như CPU, bộ nhớ, ổ đĩa và dữ liệu mạng) cũng như thông tin chẩn đoán (như lỗi khi khởi động lại container) nhằm giúp kỹ sư DevOps cô lập và giải quyết sự cố một cách nhanh chóng.

**🔒 Security Note**: Container Insights cung cấp cho bạn thông tin chi tiết từ các dịch vụ quản lý container như **Amazon EKS (Elastic Kubernetes Service)**, **Amazon ECS (Elastic Container Service)**, **AWS Fargate** và Kubernetes (K8s) độc lập, giúp bạn duy trì tính khả dụng và bảo mật cho các ứng dụng containerized.

#### Lợi ích chính

**💡 Pro Tip**: Với **Amazon CloudWatch**, bạn có thể:
- Giám sát toàn diện các tài nguyên AWS và ứng dụng của bạn
- Thiết lập cảnh báo thông minh dựa trên ngưỡng tùy chỉnh
- Tự động hóa phản hồi đối với các sự cố hoạt động
- Tạo bảng điều khiển trực quan để theo dõi hiệu suất
- Phân tích logs để khắc phục sự cố nhanh chóng

**⚠️ Warning**: Việc không thiết lập giám sát đầy đủ có thể dẫn đến thời gian ngừng hoạt động không lường trước, hiệu suất kém và chi phí cao hơn do sử dụng tài nguyên không hiệu quả.

#### Nội dung

1. [Giới thiệu](1-introduction)
2. [Các bước chuẩn bị](2-preparatory-steps)
3. [CloudWatch Metric](3-cloud-watch-metric)
4. [CloudWatch Logs](4-cloud-watch-logs)
5. [CloudWatch Alarm](5-cloud-watch-alarm)
6. [CloudWatch Dashboard](6-cloud-watch-dashboard)
7. [Dọn dẹp tài nguyên](7-clean-up-resources)
