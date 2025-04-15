---
title: "CloudWatch Metric Filter"
weight: 3
chapter: false
pre: " <b> 4.3 </b> "
---

#### CloudWatch Metric Filter

**ℹ️ Information**: CloudWatch Metric Filters cho phép bạn trích xuất dữ liệu có giá trị từ logs và chuyển đổi chúng thành các metrics có thể đo lường được, giúp bạn theo dõi và cảnh báo về các sự kiện quan trọng trong hệ thống.

1. Quay lại màn hình chính của **CloudWatch**

   - Chọn **Log groups** từ menu bên trái
   - Tìm kiếm `/ec2` trong thanh tìm kiếm
   - Chọn **/ec2/linux/var/log/messages**

![4.3.1](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.1.png)

2. Trong giao diện của **/ec2/linux/var/log/messages**

   - Mở rộng menu **Actions**
   - Chọn **Create metric filter**

![4.3.2](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.2.png)

3. Trong phần **Define Pattern**, cấu hình các thông tin sau:

   - Filter pattern: mở rộng dropdown và chọn **ERROR**
   - Test pattern: mở rộng và chọn một instance (nên chọn instance mà chúng ta đã tạo processes ở các bước trước)

![4.3.3](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.3.png)

**💡 Pro Tip**: Việc kiểm thử pattern trước khi tạo metric filter giúp bạn xác nhận rằng filter sẽ bắt đúng các sự kiện mong muốn, tránh tình trạng thiếu dữ liệu hoặc dữ liệu không chính xác.

4. Nhấn **Test pattern** để kiểm tra xem filter hoạt động chính xác không

![4.3.4](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.4.png)

5. Trong phần **Create filter name** của **Assign metric**, nhập `PythonAppErrors`

![4.3.5](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.5.png)

6. Trong phần **Metric details**, cấu hình các thông tin sau:

   - Metric namespace: `ec2-logs`
   - Metric name: `/var/log/messages - ERROR`
   - Metric value: **1**
   - Default value: **0**
   - Unit: mở rộng dropdown và chọn **Count**
   - Nhấn **Next**

![4.3.6](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.6.png)

**⚠️ Warning**: Việc đặt namespace và tên metric phù hợp rất quan trọng để dễ dàng tìm kiếm và phân loại metrics trong môi trường có nhiều ứng dụng. Hãy sử dụng quy ước đặt tên nhất quán trong toàn bộ hệ thống của bạn.

7. Xem lại cấu hình và nhấn **Create metric filter**

![4.3.7](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.7.png)

![4.3.8](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.8.png)

8. Trở lại **Metrics > All metrics**

   - Tìm kiếm với từ khóa `/var/log/messages` và `ERROR`
   - Chọn **ec2-logs > Metrics with no dimensions**

![4.3.9](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.9.png)

![4.3.10](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.10.png)

**ℹ️ Information**: Bây giờ chúng ta đã có một metric được tạo từ các log ERROR trong ứng dụng Python. Metric này có thể được sử dụng để tạo biểu đồ, dashboards, và cảnh báo khi số lượng lỗi vượt quá ngưỡng cho phép.

**💡 Pro Tip**: Bạn có thể tạo nhiều metric filters khác nhau cho cùng một log group để theo dõi các loại sự kiện khác nhau, như WARNING, INFO, hoặc các mẫu tùy chỉnh phù hợp với ứng dụng của bạn.

**🔒 Security Note**: Metric filters là công cụ quan trọng để phát hiện các vấn đề bảo mật tiềm ẩn trong hệ thống của bạn. Hãy cân nhắc tạo các filters đặc biệt cho các sự kiện liên quan đến bảo mật như đăng nhập thất bại, thay đổi quyền, hoặc truy cập trái phép.

Trong bước tiếp theo, chúng ta sẽ thiết lập CloudWatch Alarm cho metric này để nhận thông báo khi có quá nhiều lỗi xảy ra trong ứng dụng.
