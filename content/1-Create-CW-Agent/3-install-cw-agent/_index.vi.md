+++
title = "Cài đặt CloudWatch Agent"
date = 2020-04-18T00:38:32+07:00
weight = 3
chapter = false
pre = "<b>1.3. </b>"
+++

Ở bước này, bạn sẽ cài đặt CloudWatch Agent cho một EC2 Instance để instance ấy có thể gửi dữ liệu về cho CloudWatch.

**Nội dung:**
- [Cài đặt CloudWatch Agent](#cài-đặt-cloudwatch-agent)
- [Kiếm tra kết nối tới CloudWatch](#kiếm-tra-kết-nối-tới-cloudwatch)

#### Cài đặt CloudWatch Agent
1. Kết nối tới EC2 Instance mà bạn vừa tạo và tải gói CloudWatch Agent bằng lệnh sau:  
    ```bash
    sudo wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
    ```
2. Cài đặt gói agent vừa tải về bằng lệnh:  
    ```bash
    sudo rpm -U ./amazon-cloudwatch-agent.rpm
    ```
![Install CloudWatch Agent](/images/5-monitoring/1.3_cmd.png?width=90pc)

3. Tạo script để gửi memory metric về CloudWatch:  
    ```bash
    sudo vi /opt/aws/amazon-cloudwatch-agent/bin/config.json
    ```  
4. Nhấn phím **i** và copy file JSON dưới đây vào script
    ```json
    {
    "logs": {
        "logs_collected": {
            "files": {
                "collect_list": [
                    {
                        "file_path": "/var/log/httpd/access_log",
                        "log_group_name": "access_log"
                    }
                ]
            }
        }
    },
    "metrics": {
        "metrics_collected": {
            "mem": {
                "measurement": [
                    "mem_used_percent"
                ],
                "metrics_collection_interval": 30
            }
        }
    }
    }
   ```

5. Nhấn phím **ESC** rồi gõ ```:wq``` để lưu lại script.
6. Vận hành script đó để gửi thông tin lên CloudWatch bằng câu lệnh  
    ```bash
    sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s
    ```
7. Sau khi thiết lập xong, bạn sẽ có màn hình kết quả tương tự với hình dươi đây
![Install CloudWatch Agent](/images/5-monitoring/1.3_cmd2.png?width=90pc)

#### Kiếm tra kết nối tới CloudWatch
Bạn sẽ truy cập vào log file của CloudWatch Agent để kiểm tra xem bạn đã thiết lập IAM Role và CloudWatch Agent đúng chưa
1. Kết nối tới EC2 Instance mà bạn vừa tạo
2. Nhập lệnh sau để di chuyển tới thư mục chứa log file của CloudWatch Agent
    ```bash
    cd /opt/aws/amazon-cloudwatch-agent/logs/
    ```
3. Nhập lệnh sau để xem nội dung của log file.
    ```bash
    cat amazon-cloudwatch-agent.log
    ```
4. Nếu nội dung log file của bạn là tương tự như hình dưới thì bạn đã thành công.
![Install CloudWatch Agent](/images/5-monitoring/1.3_cmd3.png?width=90pc)