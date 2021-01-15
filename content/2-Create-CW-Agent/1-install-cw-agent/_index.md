+++
title = "Install CloudWatch Agent"
date = 2020-04-18T00:38:32+07:00
weight = 1
chapter = false
pre = "<b>2.1. </b>"
+++

**Contents:**
- [Install CloudWatch Agent](#install-cloudwatch-agent)

#### Install CloudWatch Agent

Each server will run the agent. You need to access to the instance that you want to install CloudWatch Agent

1. Download the agent package by command:  
```bash
sudo wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
```  

You can refer another agent package at [**Agent link download**](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/download-cloudwatch-agent-commandline.html)

2. Install package agent by running this command:  
```bash
sudo rpm -U ./amazon-cloudwatch-agent.rpm
```

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-3.PNG?width=90pc)

3. Add a script to JSON file config.json for monitoring memory:  
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

4. Deploy this script to AWS CloudWatch Agent by this command:  

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json -s
```

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-5.PNG?width=90pc)
