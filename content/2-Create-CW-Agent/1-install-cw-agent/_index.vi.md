+++
title = "Cài đặt CloudWatch Agent"
date = 2020-04-18T00:38:32+07:00
weight = 1
chapter = false
pre = "<b>2.1. </b>"
+++

**Nội dung:**
- [Cài đặt CloudWatch Agent](#cài-đặt-cloudwatch-agent)

#### Cài đặt CloudWatch Agent

Mỗi server sẽ chạy 1 agent bên trong nó. Bạn cần phải kêt nối đến server đó để cài đặt CloudWatch Agent

1. Tải gói agent bằng lệnh sau:  
```bash
sudo wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
```

Bạn có thể chọn các gói agent khác để cài đặt phù hợp với hệ điều hành của bạn tại [**Agent link download**](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/download-cloudwatch-agent-commandline.html)

2. Cài đặt gói agent vừa tải về bằng lệnh:  

```bash
sudo rpm -U ./amazon-cloudwatch-agent.rpm
```

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-3.PNG?width=90pc)

3. Gán script để gửi memory metric về CloudWatch tại file JSON config.json:  

```bash
sudo vi /opt/aws/amazon-cloudwatch-agent/bin/config.json
```  

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

4. Vận hành script đó để gửi thông tin lên CloudWatch bằng câu lệnh  
```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s
```

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-5.PNG?width=90pc)
