+++
title = "Create IAM Role"
date = 2020-04-18T00:38:32+07:00
weight = 2
chapter = false
pre = "<b>2.2. </b>"
+++

**Contents:**
- [Create IAM Role](#create-iam-role)

#### Create IAM Role

+ You need to create IAM Role on each instance that will make a permission to put custom metric to AWS CloudWatch

1. Go to the AWS Management Console and open the [**IAM Console**](https://console.aws.amazon.com/iam/home) home page.
2. In the navigation pane, choose **Roles** and then **Create role**.

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-6.PNG?width=90pc)

3. In the **Create role** task, choose use case **EC2** then click **Next Permission**.  

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-7.PNG?width=90pc)

4. Choose **Policy** name **CloudWatchAgentServerPolicy**.

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-8.PNG?width=90pc)

5. Add tags: Key and Value.
6. Add Role Information **Role name**, **Role description** then click **Create role**

![Install CloudWatch Agent](/images/5-monitoring/cloudwatch-9.PNG?width=90pc)
