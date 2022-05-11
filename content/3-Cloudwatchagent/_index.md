---
title : "Install CloudWatch Agent"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 3. </b> "
---

#### Install CloudWatch Agent

1. Initiate EC2 instance connection

- Select **Instances**
- Select the newly created instance
- Copy **Public IPv4 address**
- Use PuTTY to connect via port 22
- For detailed information about EC2 connection, please refer to [Connecting Linux virtual machine](https://000004.awsstudygroup.com/1-begin-ec2/1.1-linux-ec2/1.1.2-connect-ec2/ )

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0006-attachiamrole.png)

2. **PuTTY interface to connect EC2 instance**

- Enter **ec2-user**

![CloudWatchAgent](/images/3-Cloudwatchagent/0001-cloudwatchagent.png)

3. Since this is our first time accessing EC2 Instance we need to install the latest updates.

```
sudo yum update -y
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0002-cloudwatchagent.png)

4. Connect to the EC2 Instance you just created and load the CloudWatch Agent package with the following command:

```
sudo wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0003-cloudwatchagent.png)

5. Install the downloaded agent package with the command:

```
sudo rpm -U ./amazon-cloudwatch-agent.rpm
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0004-cloudwatchagent.png)

6. Create a script to send memory metrics to CloudWatch:

```
sudo vi /opt/aws/amazon-cloudwatch-agent/bin/config.json
```
- Press the i key and copy the following JSON file into the script:

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

- Press the ESC key and then type **:wq** to save the script.

![CloudWatchAgent](/images/3-Cloudwatchagent/0005-cloudwatchagent.png)

7. Run that script to send information to CloudWatch with the command:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json - S
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0006-cloudwatchagent.png)

8. Check Connection to CloudWatch

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status
```
- If the status is **running**, then proceed to the next step
- If status **stopped**, need to start Cloudwatch agent with the following command:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json
```


9. Enter the following command to move to the directory containing the CloudWatch Agent log file:

```
cd /opt/aws/amazon-cloudwatch-agent/logs/
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0007-cloudwatchagent.png)


10. Enter the following command to view the contents of the log file

```
cat amazon-cloudwatch-agent.log
```

![CloudWatchAgent](/images/3-Cloudwatchagent/0008-cloudwatchagent.png)