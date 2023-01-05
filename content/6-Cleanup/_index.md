---
title : "Clean up resources"
date : "`r Sys.Date()`"
weight : 6
chapter : false
pre : " <b> 6. </b> "
---

We will clean up resources in the following order:

#### Delete Dashboard

1. Go to [CloudWatch Management Console](https://aws.amazon.com/console/)
2. On the left navigation bar, select **Dashboards**
3. Select all **CloudWatch Dasboards** related to the lab.
4. Click **Delete**
5. In the prompt, click **Delete**


#### Delete IAM Role

1. Go to [IAM Management Console](https://aws.amazon.com/console/)
2. On the left navigation bar, select **Roles**
3. In the search box, find and select all Roles related to the lab.
4. Click **Delete Role**
5. In the prompt, click **Yes**, **Delete**

#### Terminate EC2 instance

1. Go to [EC2 Management Console](https://aws.amazon.com/console/)
2. On the left navigation bar, select **Instances**
3. Select all **EC2 Instance** related to the lab.
4. Click **Actions**.
5. Click **Manage Instance State**.
6. Select **Terminate**.
7. Click **Change State**