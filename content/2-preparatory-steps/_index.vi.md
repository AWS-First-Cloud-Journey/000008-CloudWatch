---
title: "Các bước chuẩn bị"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

#### Tổng quan

**ℹ️ Information**: Trong phần này, chúng ta sẽ thiết lập môi trường lab bằng cách triển khai một **AWS CloudFormation Stack**. Stack này sẽ tự động cung cấp tất cả tài nguyên AWS cần thiết để thực hành với **Amazon CloudWatch**.

#### Triển khai CloudFormation Stack

1. Truy cập vào **AWS Management Console**

   - Tìm kiếm dịch vụ **CloudFormation** trong thanh tìm kiếm
   - Chọn **CloudFormation** từ kết quả tìm kiếm

![2.1](/images/2-preparatory-steops/2.1.png)

2. Trong giao diện **CloudFormation**

   - Chọn **Create stack**
   - Chọn **With new resources (standard)**

![2.2](/images/2-preparatory-steops/2.2.png)

3. Trong giao diện **Create stack**

   **💡 Pro Tip**: Tải file template về máy trước khi tiếp tục để quá trình triển khai diễn ra suôn sẻ.
   
   - Tải file cấu hình [template](https://raw.githubusercontent.com/AWS-First-Cloud-Journey/CloudWatchWorkshop/main/template.yml) về máy
   - Trong phần **Prerequisite - Prepare template**, chọn **Choose an existing template**
   - Tiếp theo chọn **Upload a template file**
   - Ấn **Choose file** để tải lên file template đã tải về
   - Ấn **Next**

![2.3](/images/2-preparatory-steops/2.3.png)

4. Cấu hình thông tin Stack

   - **Stack name**: Nhập `FCJ-CloudWatch-Workshop` (hoặc một tên dễ nhớ khác)
   - **RegionId**: Chọn đúng Region ID nơi bạn đang thực hiện workshop (ví dụ: **us-east-1** cho N. Virginia)
   - Giữ nguyên các tham số còn lại với giá trị mặc định
   - Ấn **Next**

![2.4](/images/2-preparatory-steops/2.4.png)

5. Cấu hình tùy chọn Stack

   **⚠️ Warning**: Đảm bảo bạn đã tích vào ô xác nhận IAM resources để CloudFormation có thể tạo các tài nguyên IAM cần thiết.
   
   - Không cần thay đổi cấu hình mặc định trên trang này
   - Cuộn xuống dưới cùng
   - Tích chọn **I acknowledge that AWS CloudFormation might create IAM resources with custom names**
   - Ấn **Next**

![2.5](/images/2-preparatory-steops/2.5.png)

6. Xem lại và tạo Stack

   - Kiểm tra lại tất cả thông tin cấu hình
   - Cuộn xuống dưới cùng và ấn **Submit** để bắt đầu tạo Stack

![2.6](/images/2-preparatory-steops/2.6.png)

7. Theo dõi quá trình triển khai

   **ℹ️ Information**: Quá trình triển khai Stack có thể mất khoảng 5 phút để hoàn tất. Trong thời gian này, CloudFormation sẽ tự động tạo tất cả tài nguyên cần thiết cho workshop.

![2.7](/images/2-preparatory-steops/2.7.png)

#### Xác nhận triển khai thành công

**🔒 Security Note**: Sau khi triển khai thành công, hãy kiểm tra tab **Outputs** của Stack để lấy thông tin về các tài nguyên đã được tạo, bao gồm các URL và thông tin truy cập cần thiết cho các bước tiếp theo.

![2.8](/images/2-preparatory-steops/2.8.png)

**💡 Pro Tip**: Khi Stack hiển thị trạng thái **CREATE_COMPLETE** với màu xanh lá, điều này xác nhận rằng tất cả tài nguyên đã được triển khai thành công và bạn đã sẵn sàng để tiếp tục với các bài thực hành **Amazon CloudWatch**.

#### Tạo bucket và tải file logger.py
1. Tìm kiếm S3 trên search bar
![2.9](/images/2-preparatory-steops/2.9.png)
2. Nhấn create bucket

3. Tên bucket phải là duy nhất trên không gian toàn cầu, không được trùng.

![2.10](/images/2-preparatory-steops/2.10.png)

4. Mọi cài đặt để nguyên mặc định

5. Nhấn crete bucket ở cuối trang

![2.11](/images/2-preparatory-steops/2.11.png)

6. Chọn bucket vừa được tạo ra

7. Nhấn upload và tải file logger.py lên bucket

8. Kiểm tra file tải đã hoàn tất

![2.12](/images/2-preparatory-steops/2.12.png)

