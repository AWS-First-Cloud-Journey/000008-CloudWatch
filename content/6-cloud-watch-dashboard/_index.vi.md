---
title: "CloudWatch Dashboards"
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

#### CloudWatch Dashboards

**ℹ️ Information**: Amazon CloudWatch Dashboards là công cụ trực quan hóa mạnh mẽ cho phép bạn tạo các bảng điều khiển tùy chỉnh để giám sát tài nguyên AWS trong thời gian thực. Dashboards giúp tập hợp các metrics, logs và alarms quan trọng vào một nơi duy nhất, tạo điều kiện thuận lợi cho việc giám sát và phân tích hệ thống.

Trong phần cuối của workshop này, chúng ta sẽ tạo một Dashboard đơn giản để tập trung quản lý các Metrics và Alarms đã thiết lập trước đó, đặc biệt là Error Logs đã cấu hình trong phần trước.

1. Thêm alarm đã tạo vào Dashboard:

   - Chọn **PythonApplicationErrorAlarm**
   - Mở rộng menu **Actions**
   - Chọn **Add to dashboard**

![6.1](/images/6-cloud-watch-dashboard/6.1.png)

2. Trong hộp thoại **Add to dashboard**, chọn **Create new**

![6.2](/images/6-cloud-watch-dashboard/6.2.png)

3. Cấu hình Dashboard mới:

   - Nhập tên dashboard: `CloudWatch-Workshop`
   - Nhấn **Create**
   - Nhấn **Add to dashboard**

![6.3](/images/6-cloud-watch-dashboard/6.3.png)

![6.4](/images/6-cloud-watch-dashboard/6.4.png)

**💡 Pro Tip**: Đặt tên dashboard có ý nghĩa và phân loại rõ ràng sẽ giúp bạn dễ dàng quản lý khi số lượng dashboards tăng lên trong môi trường thực tế. Cân nhắc sử dụng các tiền tố như "Prod-", "Dev-", hoặc tên ứng dụng để phân loại.

Dưới đây là dashboard vừa được tạo:

![6.5](/images/6-cloud-watch-dashboard/6.5.png)

**ℹ️ Information**: CloudWatch Dashboards hỗ trợ nhiều loại widget khác nhau như biểu đồ, số liệu đơn, bảng, văn bản và nhiều hơn nữa. Mỗi widget có thể được tùy chỉnh về kích thước, vị trí và hiển thị dữ liệu.

Bạn có thể thực hiện nhiều thao tác tùy chỉnh trên widget này:

![6.6](/images/6-cloud-watch-dashboard/6.6.png)

![6.7](/images/6-cloud-watch-dashboard/6.7.png)

**🔒 Security Note**: Dashboards có thể được chia sẻ với người dùng khác trong tổ chức của bạn hoặc thậm chí công khai (không yêu cầu đăng nhập AWS). Hãy cẩn thận khi chia sẻ dashboards có chứa thông tin nhạy cảm về cơ sở hạ tầng của bạn.

**⚠️ Warning**: CloudWatch Dashboards có giới hạn 500 widgets trên mỗi dashboard và 20.000 metrics trên tất cả các dashboards. Trong môi trường sản xuất lớn, hãy cân nhắc tạo nhiều dashboards chuyên biệt thay vì một dashboard quá lớn và phức tạp.

Chúc mừng! Bạn đã hoàn thành bài workshop về Amazon CloudWatch. Giờ đây bạn đã nắm vững các kỹ năng cơ bản để giám sát, phân tích và cảnh báo trong môi trường AWS của mình.
