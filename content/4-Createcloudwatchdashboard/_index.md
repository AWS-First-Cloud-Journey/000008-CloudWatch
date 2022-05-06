---
title : "CloudWatch Dashboard"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 4. </b> "
---

#### Create CloudWatch Dashboard
To get started with CloudWatch Dashboard, you first need to create a new dashboard. You can create multiple dashboards. There is no limit to the number of dashboards in an AWS account. All dashboards are Global, not located in a specific region


1. Access the interface [AWS Management Console](https://aws.amazon.com/console/)

- Find **CloudWatch**
- Select **CloudWatch**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0001-createcloudwatchdashboard.png)

2. In the **CloudWatch** interface

- Select **Dashboard**
- Select **Custom dashboard**
- Select **Create dashboard**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0002-createcloudwatchdashboard.png)

3. In the **Create new dashboard** interface

- **Dashboard name**, enter ```MyFirstDashboard```
- Select **Create dashboard**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0003-createcloudwatchdashboard.png)

4. At the **Add Widget** prompt, select the **Line** interface type. In the **Add to this dashboard** interface

- Select **Metrics**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0004-createcloudwatchdashboard.png)

5. In **Add metric graph** interface

- Select **Browse**
- **Custom namespaces**, select **CWAgent**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0005-createcloudwatchdashboard.png)

6. Next, select **host**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0006-createcloudwatchdashboard.png)

7. Select the host according to **Hostname type** of the newly created instance

- Select **Create widget**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0007-createcloudwatchdashboard.png)

8. Finish creating the CloudWatch dashboard

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0008-createcloudwatchdashboard.png)

9. Zoom in on the dashboard for easy viewing and select **View in metrics**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/0009-createcloudwatchdashboard.png)

10. In the **CloudWatch metrics** interface

- Observe the interface and features

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00010-createcloudwatchdashboard.png)

11. In the **CloudWatch metrics** interface

- Select **Add query**
- Select **EC2**
- Select **Average Active CPU for an application (CloudWatch Agent)**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00011-createcloudwatchdashboard.png)

12. Query results are displayed

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00012-createcloudwatchdashboard.png)

13. Continue, in **CloudWatch metrics** view

- Select **Add math**
- Select **Search**
- Select **EC2 CPU utilization**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00013-createcloudwatchdashboard.png)

14. The results are displayed, select **CWgent hostname type** of the instance and observe the graph

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00014-createcloudwatchdashboard.png)

15. Return to **CloudWatch Dashboard** interface

- Select **Save dashboard**

![CreateCloudWatchDashboard](/images/4-Createcloudwatchdashboard/00015-createcloudwatchdashboard.png)

