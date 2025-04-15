---
title: "CloudWatch Metric Filter"
weight: 3
chapter: false
pre: " <b> 4.3 </b> "
---

#### Creating a CloudWatch Metric Filter

**ℹ️ Information**: CloudWatch Metric Filters allow you to extract and transform log data into numerical CloudWatch metrics that you can graph or set alarms on.

1. Return to the main screen of **Amazon CloudWatch**

   - Select **Log groups** from the navigation pane
   - Search for `/ec2` in the filter box
   - Select **/ec2/linux/var/log/messages** log group

![4.3.1](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.1.png)

2. In the **/ec2/linux/var/log/messages** log group interface

   - Click on **Actions** dropdown menu
   - Select **Create metric filter**

![4.3.2](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.2.png)

3. In the **Define Pattern** section, configure the following:

   - Filter pattern: select **ERROR** from the dropdown menu
   - Test pattern: select any log stream instance (preferably the instance where we created processes in the previous steps)

![4.3.3](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.3.png)

4. Click **Test pattern** to validate the filter configuration

![4.3.4](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.4.png)

5. In the **Create filter name** section of **Assign metric**, enter `PythonAppErrors`

![4.3.5](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.5.png)

6. In the **Metric details** section, configure the following:

   - Metric namespace: `ec2-logs`
   - Metric name: `/var/log/messages - ERROR`
   - Metric value: **1**
   - Default value: **0**
   - Unit: select **Count** from the dropdown menu
   - Click **Next**

![4.3.6](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.6.png)

7. Review your configuration and click **Create metric filter**

![4.3.7](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.7.png)

![4.3.8](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.8.png)

8. Navigate to **Metrics > All metrics** in the CloudWatch console

   - Search for the keywords `/var/log/messages` and `ERROR`
   - Select **ec2-logs > Metrics with no dimensions**

![4.3.9](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.9.png)

![4.3.10](/images/4-cloud-watch-logs/4.3-metric-filter/4.3.10.png)

**💡 Pro Tip**: You can create multiple metric filters for different error patterns or log events to gain comprehensive visibility into your application's behavior.

**🔒 Security Note**: Ensure that your metric filters don't extract sensitive information that might be present in your logs.

Now we have a metric that captures ERROR logs from the application. In the next step, we will set up a CloudWatch Alarm for this metric to receive notifications when errors occur.
