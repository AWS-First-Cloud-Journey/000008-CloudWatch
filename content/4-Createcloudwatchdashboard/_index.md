---
title : "Create CloudWatch Dashboard"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 4. </b> "
---

#### Create CloudWatch Dashboard

To get started with CloudWatch Dashboard, you first need to create a new dashboard. You can create multiple dashboards. There is no limit to the number of dashboards in an AWS account. All dashboards are Global, not located in a specific region


1. Access the [AWS Management Console] interface(https://aws.amazon.com/console/)

   - Find **CloudWatch**
   - Select **CloudWatch**

![CreateCloudWatchDashboard](/images/6/0001.png?featherlight=false&width=90pc)

2. In the **CloudWatch** interface

   - Select **Dashboard**
   - Select **Custom dashboard**
   - Select **Create dashboard**

![CreateCloudWatchDashboard](/images/6/0002.png?featherlight=false&width=90pc)

3. In the **Create new dashboard** interface

   - **Dashboard name**, enter ```MyFirstDashboard```
   - Select **Create dashboard**

![CreateCloudWatchDashboard](/images/6/0003.png?featherlight=false&width=90pc)

4. At the **Add Widget** prompt, select the **Line** interface type. In the **Add to this dashboard** interface

   - Select **Metrics**

![CreateCloudWatchDashboard](/images/6/0004.png?featherlight=false&width=90pc)

5. In the **Add metric graph** interface

   - Select **Browse**
   - **Custom namespaces**, select **CWAgent**

![CreateCloudWatchDashboard](/images/6/0005.png?featherlight=false&width=90pc)

6. Next, select **host**

![CreateCloudWatchDashboard](/images/6/0006.png?featherlight=false&width=90pc)

7. Select the host according to **Hostname type** of the newly created instance

   - Select **Create widget**

![CreateCloudWatchDashboard](/images/6/0007.png?featherlight=false&width=90pc)

8. Finish creating the CloudWatch dashboard

![CreateCloudWatchDashboard](/images/6/0009.png?featherlight=false&width=90pc)

9. Zoom in on the dashboard for easy viewing and select **View in metrics**

![CreateCloudWatchDashboard](/images/6/00010.png?featherlight=false&width=90pc)

10. In the **CloudWatch metrics** interface

    - Observe the interface and features

![CreateCloudWatchDashboard](/images/6/00011.png?featherlight=false&width=90pc)

11. In the **CloudWatch metrics** interface

    - Select **Add query**
    - Select **EC2**
    - Select **Average Active CPU for an application (CloudWatch Agent)**

![CreateCloudWatchDashboard](/images/6/00012.png?featherlight=false&width=90pc)

12. Query results are displayed

![CreateCloudWatchDashboard](/images/6/00013.png?featherlight=false&width=90pc)

13. Continue, in the **CloudWatch metrics** View

    - Select **Add math**
    - Select **Search**
    - Select **EC2 CPU utilization**

![CreateCloudWatchDashboard](/images/6/00014.png?featherlight=false&width=90pc)

14. Results displayed, select **CWgent hostname type** of the instance and observe the graph

![CreateCloudWatchDashboard](/images/6/00015.png?featherlight=false&width=90pc)

15. Return to **CloudWatch Dashboard** interface

    - Select **Save dashboard**

![CreateCloudWatchDashboard](/images/6/00016.png?featherlight=false&width=90pc)