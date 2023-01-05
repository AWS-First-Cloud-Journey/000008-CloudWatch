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
- Sử dụng PuTTY hoặc MobaXterm để kết nối qua port 22
- Thông tin chi tiết vê kết nối EC2 bạn tham khảo [Kết nối máy ảo Linux](https://000004.awsstudygroup.com/1-begin-ec2/1.1-linux-ec2/1.1.2-connect-ec2/)

![Attach IAM Role](/images/5/0001.png?featherlight=false&width=90pc)

2. Giao diện MobaXterm.

![CloudWatchAgent](/images/5/0002.png?featherlight=false&width=90pc)

- Chọn SSH

![CloudWatchAgent](/images/5/0003.png?featherlight=false&width=90pc)

- Nhập **ec2-user**

![CloudWatchAgent](/images/5/0004.png?featherlight=false&width=90pc)



3. Do đây là lần đầu ta truy cập EC2 Instance chúng ta cần thực hiện cài đặt các cập nhật mới nhất.

![CloudWatchAgent](/images/5/0005.png?featherlight=false&width=90pc)

```
sudo yum update -y
```

![CloudWatchAgent](/images/5/0006.png?featherlight=false&width=90pc)

4. Kết nối tới EC2 Instance mà bạn vừa tạo và tải gói CloudWatch Agent bằng lệnh sau:

```
sudo wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
```

![CloudWatchAgent](/images/5/0007.png?featherlight=false&width=90pc)

5. Cài đặt gói agent vừa tải về bằng lệnh:

```
sudo rpm -U ./amazon-cloudwatch-agent.rpm
```

![CloudWatchAgent](/images/5/0008.png?featherlight=false&width=90pc)

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

![CloudWatchAgent](/images/5/0009.png?featherlight=false&width=90pc)

- Nhấn phím ESC rồi gõ **:wq** để lưu lại script.

![CloudWatchAgent](/images/5/00010.png?featherlight=false&width=90pc)



7. Vận hành script đó để gửi thông tin lên CloudWatch bằng câu lệnh:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s
```
![CloudWatchAgent](/images/5/00011.png?featherlight=false&width=90pc)



8. Kiểm tra kết nối tới CloudWatch

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status
```

![CloudWatchAgent](/images/5/00012.png?featherlight=false&width=90pc)

- Nếu trạng thái **running** thì thực hiện bước tiếp theo
- Nếu trạng thái **stopped** thì cần start Cloudwatch agent bằng câu lệnh sau:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json
```


![CloudWatchAgent](/images/5/00013.png?featherlight=false&width=90pc)


9. Nhập lệnh sau để di chuyển tới thư mục chứa log file của CloudWatch Agent:

```
cd /opt/aws/amazon-cloudwatch-agent/logs/
```


![CloudWatchAgent](/images/5/00014.png?featherlight=false&width=90pc)

10. Nhập lệnh sau để xem nội dung của log file

```
cat amazon-cloudwatch-agent.log
```




![CloudWatchAgent](/images/5/00015.png?featherlight=false&width=90pc)
