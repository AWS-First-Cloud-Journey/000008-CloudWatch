---
title: "CloudWatch Logs"
weight: 1
chapter: false
pre: " <b> 4.1 </b> "
---

#### CloudWatch Logs

**ℹ️ Information**: Amazon CloudWatch Logs cho phép bạn tập trung và phân tích logs từ các tài nguyên AWS, giúp bạn hiểu rõ hơn về hoạt động của hệ thống và khắc phục sự cố nhanh chóng.

1. Trong trang chính của CloudWatch.

   - Phần menu bên trái, mở rộng mục **Logs**
   - Chọn **Log groups**

![4.1.1](/images/4-cloud-watch-logs/4.1-logs/4.1.1.png)

2. Trên thanh tìm kiếm, nhập `/ec2` và chọn **/ec2/linux/var/log/messages**

![4.1.2](/images/4-cloud-watch-logs/4.1-logs/4.1.2.png)

![4.1.3](/images/4-cloud-watch-logs/4.1-logs/4.1.3.png)

**💡 Pro Tip**: Sử dụng thanh tìm kiếm giúp bạn nhanh chóng tìm thấy các log groups cụ thể trong môi trường có nhiều tài nguyên, tiết kiệm thời gian phân tích.

3. Chọn một instance bất kỳ để xem chi tiết logs

![4.1.4](/images/4-cloud-watch-logs/4.1-logs/4.1.4.png)

4. Trong giao diện logs, bạn có thể thấy các bản ghi từ instance này được tạo ra từ nhiều nguồn khác nhau như: dhclient, NET, ec2net, systemd...

![4.1.5](/images/4-cloud-watch-logs/4.1-logs/4.1.5.png)

**ℹ️ Information**: Các logs này cung cấp thông tin chi tiết về hoạt động của hệ thống, giúp bạn theo dõi các sự kiện, phát hiện lỗi và hiểu rõ hơn về cách hệ thống đang hoạt động.

5. Trở lại thông tin của log group **/ec2/linux/var/log/messages**. Bây giờ chúng ta sẽ cấu hình thời gian lưu trữ (retention) cho các log events

   - Mở rộng menu **Actions**
   - Chọn **Edit retention setting**

![4.1.6](/images/4-cloud-watch-logs/4.1-logs/4.1.6.png)

6. Trong phần **Retention setting**, chọn **1 week (7 days)** cho **Expire events after**

![4.1.7](/images/4-cloud-watch-logs/4.1-logs/4.1.7.png)

![4.1.8](/images/4-cloud-watch-logs/4.1-logs/4.1.8.png)

**⚠️ Warning**: Việc cấu hình thời gian lưu trữ logs là rất quan trọng để tối ưu chi phí. Logs lưu trữ quá lâu sẽ làm tăng chi phí lưu trữ, trong khi thời gian lưu trữ quá ngắn có thể khiến bạn mất dữ liệu quan trọng khi cần phân tích sự cố.

**🔒 Security Note**: Đối với các môi trường yêu cầu tuân thủ quy định, bạn nên xem xét các yêu cầu về thời gian lưu trữ logs trước khi thiết lập chính sách retention.

**💡 Pro Tip**: Bạn có thể xuất logs sang Amazon S3 để lưu trữ dài hạn với chi phí thấp hơn, đồng thời vẫn duy trì khả năng truy xuất khi cần thiết.
