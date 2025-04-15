---
title: "Xem các Metrics"
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

#### Xem các Metrics

**ℹ️ Information**: Trong phần này, chúng ta sẽ thực hành cách xem và phân tích các metrics trong Amazon CloudWatch, giúp bạn hiểu rõ hơn về hiệu suất của các tài nguyên AWS.

1. Truy cập **AWS Management Console**

   - Tìm kiếm dịch vụ **CloudWatch** trong thanh tìm kiếm
   - Chọn **CloudWatch** từ kết quả tìm kiếm

![3.1.1](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.1.png)

2. Trong giao diện **CloudWatch**

   - Mở rộng phần **Metrics** ở menu bên trái
   - Chọn **All metrics**

![3.1.2](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.2.png)

3. Trong giao diện biểu đồ metrics, nhập `EC2` vào ô tìm kiếm

![3.1.3](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.3.png)

4. Từ kết quả tìm kiếm, chọn **EC2 > Per-Instance Metrics**

![3.1.4](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.4.png)

![3.1.5](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.5.png)

5. Trên thanh tìm kiếm, nhập `CPUUtilization` và tìm kiếm

![3.1.6](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.6.png)

**💡 Pro Tip**: Khi sử dụng thanh tìm kiếm, CloudWatch mặc định sẽ tìm theo **Metric name**, giúp bạn nhanh chóng lọc ra các metrics cụ thể cần theo dõi.

![3.1.7](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.7.png)

6. Chọn 2 trong số 5 instances được tạo ra từ CloudFormation stack để so sánh thông số CPUUtilization

**ℹ️ Information**: Từ biểu đồ, chúng ta có thể thấy cả hai instances bắt đầu hoạt động mạnh vào khoảng 2:40, đây là thời điểm có mức sử dụng CPU cao nhất. Sau đó, mức sử dụng CPU giảm dần và ổn định vào khoảng 3:30, cho thấy các instances đã hoàn thành phần lớn công việc được giao.

![3.1.8](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.8.png)

7. Tiếp theo, chúng ta sẽ xem các metrics khác của cùng một Instance

   - Bỏ chọn dòng của Instance B
   - Xóa tag tìm kiếm **CPUUtilization**
   - Nhập `EBSWriteBytes` vào thanh tìm kiếm

![3.1.9](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.9.png)

![3.1.10](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.10.png)

8. Kéo xuống và chọn Instance A

**💡 Pro Tip**: Khi phân tích nhiều metrics cùng lúc, bạn có thể thấy mối tương quan giữa các hoạt động khác nhau của instance. Trong trường hợp này, chúng ta thấy rằng hoạt động ghi vào EBS và mức sử dụng CPU có mối tương quan trong giai đoạn đầu khi instance khởi động, nhưng không hoàn toàn trùng khớp ở tất cả các thời điểm.

![3.1.11](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.11.png)

Bạn có thể ẩn một trong hai metrics để xem chi tiết hơn.

![3.1.12](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.12.png)

**⚠️ Warning**: Khi hiển thị nhiều metrics có đơn vị đo khác nhau trên cùng một biểu đồ, việc phân tích có thể trở nên khó khăn. Trong phần tiếp theo, chúng ta sẽ tìm hiểu cách tùy chỉnh biểu đồ để có cái nhìn trực quan hơn.

#### Thao tác với biểu đồ

**ℹ️ Information**: CloudWatch cho phép bạn tùy chỉnh biểu đồ để hiển thị dữ liệu một cách hiệu quả hơn, đặc biệt khi so sánh các metrics có đơn vị đo và phạm vi giá trị khác nhau.

1. Trong tab **Graphed metrics**, tại dòng **EBSWriteBytes**, cột **Y axis**, chọn **>** để chuyển metric này sang trục Y thứ hai

![3.1.13](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.13.png)

2. Thêm đánh dấu ngang (horizontal annotation) cho biểu đồ

   - Chuyển sang tab **Options**
   - Chọn **Add horizontal annotation**

![3.1.14](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.14.png)

3. Cấu hình horizontal annotation với các thông tin sau:

   - Label: **5% Mark**
   - Value: **5**

**💡 Pro Tip**: Sử dụng annotations để đánh dấu các ngưỡng quan trọng giúp bạn dễ dàng xác định khi nào metrics vượt quá hoặc giảm xuống dưới các mức cần quan tâm.

![3.1.15](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.15.png)

4. Tạo thêm Vertical annotation với label là `Job start`

![3.1.16](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.16.png)

5. Điều chỉnh thời gian cho vertical annotation

   - Di chuột vào phần đầu của đường chỉ trên biểu đồ
   - Quan sát thấy công việc bắt đầu vào khoảng **02:40**

![3.1.17](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.17.png)

   - Sửa thông tin giờ của Date của Job start thành **02:40**
   - Chọn **Apply** để áp dụng thay đổi

![3.1.18](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.18.png)

Đường Job start đã được di chuyển đến vị trí chính xác.

![3.1.19](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.19.png)

**🔒 Security Note**: Việc theo dõi chính xác thời điểm bắt đầu và kết thúc của các công việc không chỉ giúp tối ưu hiệu suất mà còn hỗ trợ phát hiện các hoạt động bất thường, góp phần nâng cao bảo mật cho hệ thống của bạn.

**💡 Pro Tip**: Bạn có thể xóa các đánh dấu này trước khi chuyển sang phần tiếp theo, nơi chúng ta sẽ tập trung vào việc làm việc với các biểu thức phức tạp hơn trong CloudWatch.
