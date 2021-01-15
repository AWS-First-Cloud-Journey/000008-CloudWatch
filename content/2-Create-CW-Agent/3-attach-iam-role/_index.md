+++
title = "Attach IAM Role"
date = 2020-04-18T00:38:32+07:00
weight = 3
chapter = false
pre = "<b>2.3. </b>"
+++

**Contents:**
- [Attach IAM Role to Instance](#attach-iam-role-to-instance)

#### Attach IAM Role to Instance

1. Go to the AWS Management Console and open the [**EC2 Instance Console**](https://console.aws.amazon.com/ec2) home page.
2. In the navigation pane, choose **Instances**, choose Instance that you want to Attach IAM Role, then click to **Action** -> **Instance Setting** -> **Attach/Replace IAM Role**.

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-10.PNG?width=90pc)

3. Choose IAM Role which you have created, then click **Apply**.  

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-11.PNG?width=90pc)

4. Go to the AWS Management Console and open the [**CloudWatch Console**](https://console.aws.amazon.com/cloudwatch/home)
5. In the navigation pane, choose **Metrics**.
6. After few second, you will see a **custom metric** that monitor meomory. Click to this **custome metric**, you can see memory metric which is sent to CloudWatch.  

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-13.PNG?width=90pc)

