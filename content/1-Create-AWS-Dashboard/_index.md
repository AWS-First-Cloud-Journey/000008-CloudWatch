+++
title = "CloudWatch Dashboard"
date = 2020-04-18T00:38:32+07:00
weight = 1
chapter = false
pre = "<b>1. </b>"
+++

**Contents:**
- [Create AWS CloudWatch Dashboard](#create-aws-cloudwatch-dashboard)

#### Create AWS CloudWatch Dashboard

To get started with CloudWatch dashboards, you must first create a dashboard. You can create multiple dashboards. There is no limit on the number of CloudWatch dashboards in your AWS account. All dashboards are global, not Region-specific.

1. Go to the AWS Management Console and open the [**CloudWatch console**](https://console.aws.amazon.com/cloudwatch/home) home page.
2. In the navigation pane, choose **Dashboards** and then **Create dashboard**.
3. In the **Create new dashboard** dialog box, enter a name for the dashboard and choose **Create dashboard**.  
4. Do one of the following in the **Add to this dashboard** dialog box:
  * To add a graph to your dashboard, choose **Line** or **Stacked area** and choose **Configure**. In the **Add metric graph** dialog box, select the metrics to graph and choose **Create widget**. If a specific metric doesn't appear in the dialog box because it hasn't published data in more than 14 days, you can add it manually. For more information, see [Graph Metrics Manually on a CloudWatch Dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_old_metrics_to_graph.html).
  * To add a number displaying a metric to the dashboard, choose **Number** and then **Configure**. In the **Add metric graph** dialog box, select the metrics to graph and choose **Create widget**.
  * To add a text block to your dashboard, choose **Text** and then **Configure**. In the **New text widget** dialog box, for ****Markdown**, add and format your text using [Markdown](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/aws-markdown.html). Choose **Create widget**.

![Create CloudWatch Dashboard](/images/5-monitoring/cloudwatch-1.PNG?width=90pc)

5. Optionally, choose **Add widget** and repeat step 4 to add another widget to the dashboard. You can repeat this step multiple times.
6. Choose **Save dashboard**.

![Create CloudWatch Dashboard](/images/5-monitoring/cloudwatch-2.PNG?width=90pc)
