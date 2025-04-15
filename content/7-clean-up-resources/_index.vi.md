---
title: "Dọn dẹp tài nguyên"
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

#### Dọn dẹp tài nguyên

**ℹ️ Information**: Sau khi hoàn thành workshop, việc dọn dẹp tài nguyên là bước quan trọng để tránh phát sinh chi phí không cần thiết. Trong phần này, chúng ta sẽ xóa CloudFormation stack đã tạo ở đầu bài.

**⚠️ Warning**: Mặc dù các tài nguyên EC2 và các dịch vụ liên quan sẽ bị xóa ngay lập tức, CloudWatch Metrics và Logs sẽ vẫn tồn tại trong hệ thống AWS của bạn tối đa 15 tháng theo chính sách lưu trữ mặc định.

1. Trên thanh tìm kiếm dịch vụ AWS:

   - Nhập `CloudFormation`.
   - Chọn **CloudFormation**.

![7.1](/images/7-clean-up-resources/7.1.png)

2. Trong CloudFormation Console:

   - Chọn stack đã tạo trong workshop này.
   - Ấn chọn **Delete**.

![7.2](/images/7-clean-up-resources/7.2.png)

3. Trong hộp thoại xác nhận:

   - Ấn chọn **Delete** để xác nhận việc xóa stack.

![7.3](/images/7-clean-up-resources/7.3.png)

**💡 Pro Tip**: Quá trình xóa stack có thể mất vài phút tùy thuộc vào số lượng và độ phức tạp của tài nguyên. Bạn có thể theo dõi tiến trình trong tab "Events" của stack.

4. Chờ đợi quá trình xóa hoàn tất:

   - Stack sẽ hiển thị trạng thái "DELETE_IN_PROGRESS" trong quá trình xóa.
   - Sau khi hoàn tất, stack sẽ biến mất khỏi danh sách.

![7.4](/images/7-clean-up-resources/7.4.png)

**🔒 Security Note**: Việc dọn dẹp tài nguyên không chỉ giúp tiết kiệm chi phí mà còn là biện pháp bảo mật tốt, giảm thiểu bề mặt tấn công tiềm ẩn trong môi trường AWS của bạn.
