---
title : "Installing CloudWatch Agent"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 3. </b> "
---

#### Install CloudWatch Agent

1. Start the EC2 instance connection

- Select **Instances**
- Select the newly created instance
- Copy **Public IPv4 address**
- Use PuTTY or MobaXterm to connect via port 22
- For detailed information about EC2 connection, please refer to [Connecting Linux Virtual Machine](https://000004.awsstudygroup.com/1-begin-ec2/1.1-linux-ec2/1.1.2-connect-ec2/ )

![Attach IAM Role](/images/5/0001.png?featherlight=false&width=90pc)

2. MobaXterm interface.

![CloudWatchAgent](/images/5/0002.png?featherlight=false&width=90pc)

- Select SSH

![CloudWatchAgent](/images/5/0003.png?featherlight=false&width=90pc)

- Enter **ec2-user**

![CloudWatchAgent](/images/5/0004.png?featherlight=false&width=90pc)



3. Since this is our first time accessing EC2 Instance we need to install the latest updates.

![CloudWatchAgent](/images/5/0005.png?featherlight=false&width=90pc)

```
sudo yum update -y
```

![CloudWatchAgent](/images/5/0006.png?featherlight=false&width=90pc)

4. Connect to the EC2 Instance you just created and load the CloudWatch Agent package with the following command:

```
sudo wget https://s3.amazonaws.com/amazoncloudwatch-agent/amazon_linux/amd64/latest/amazon-cloudwatch-agent.rpm
```

![CloudWatchAgent](/images/5/0007.png?featherlight=false&width=90pc)

5. Install the downloaded agent package with the command:

```
sudo rpm -U ./amazon-cloudwatch-agent.rpm
```

![CloudWatchAgent](/images/5/0008.png?featherlight=false&width=90pc)

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

![CloudWatchAgent](/images/5/0009.png?featherlight=false&width=90pc)

- Press the ESC key and then type **:wq!** to save the script.

![CloudWatchAgent](/images/5/00010.png?featherlight=false&width=90pc)



7. Run that script to send information to CloudWatch with the command:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json - S
```
![CloudWatchAgent](/images/5/00011.png?featherlight=false&width=90pc)



8. Check Connection to CloudWatch

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -m ec2 -a status
```

![CloudWatchAgent](/images/5/00012.png?featherlight=false&width=90pc)

- If the status is **running**, then proceed to the next step
- If the status is **stopped**, you need to start the Cloudwatch agent with the following command:

```
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config. json
```


![CloudWatchAgent](/images/5/00013.png?featherlight=false&width=90pc)


9. Enter the following command to move to the directory containing the CloudWatch Agent log file:

```
cd /opt/aws/amazon-cloudwatch-agent/logs/
```


![CloudWatchAgent](/images/5/00014.png?featherlight=false&width=90pc)

10. Enter the following command to view the contents of the log file

```
cat amazon-cloudwatch-agent.log
```

![CloudWatchAgent](/images/5/00015.png?featherlight=false&width=90pc)