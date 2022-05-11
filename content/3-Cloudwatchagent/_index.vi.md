---
title : "Cài đặt CloudWatch Agent"
date :  "`r Sys.Date()`" 
weight : 3 
chapter : false
pre : " <b> 3. </b> "
---

#### Cài đặt CloudWatch Agent

1. Bắt đầu kết nối EC2 instance 

- Chọn **Instances**
- Chọn instance vừa tạo
- Sao chép **Public IPv4 address**
- Sử dụng PuTTY để kết nối qua port 22
- Thông tin chi tiết vê kết nối EC2 bạn tham khảo [Kết nối máy ảo Linux](https://000004.awsstudygroup.com/1-begin-ec2/1.1-linux-ec2/1.1.2-connect-ec2/)

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0006-attachiamrole.png)

2. Giao diện **PuTTY kết nối EC2 instance**

- Nhập **ec2-user**

![CloudWatchAgent](/images/3-Cloudwatchagent/0001-cloudwatchagent.png)

3. Do đây là lần đầu ta truy cập EC2 Instance chúng ta cần thực hiện cài đặt các cập nhật mới nhất.

```
sudo yum update -y
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0002-cloudwatchagent.png)

4. Kết nối tới EC2 Instance mà bạn vừa tạo và tải gói CloudWatch Agent bằng lệnh sau:

```
sudo wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0003-cloudwatchagent.png)

5. Cài đặt gói agent vừa tải về bằng lệnh:

```
sudo rpm -U ./amazon-cloudwatch-agent.rpm
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0004-cloudwatchagent.png)

6. Tạo script để gửi memory metric về CloudWatch:

```
sudo vi /opt/aws/amazon-cloudwatch-agent/bin/config.json
```
- Nhấn phím i và copy file JSON dưới đây vào script:

```
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

- Nhấn phím ESC rồi gõ **:wq** để lưu lại script.

![CloudWatchAgent](/images/3-Cloudwatchagent/0005-cloudwatchagent.png)

7. Vận hành script đó để gửi thông tin lên CloudWatch bằng câu lệnh:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0006-cloudwatchagent.png)

8. Kiểm tra kết nối tới CloudWatch

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status
```
- Nếu trạng thái **running** thì thực hiện bước tiếp theo
- Nếu trạng thái **stopped** thì cần start Cloudwatch agent bằng câu lệnh sau:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json
```

9. Nhập lệnh sau để di chuyển tới thư mục chứa log file của CloudWatch Agent:

```
cd /opt/aws/amazon-cloudwatch-agent/logs/
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0007-cloudwatchagent.png)


10. Nhập lệnh sau để xem nội dung của log file

```
cat amazon-cloudwatch-agent.log
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0008-cloudwatchagent.png)