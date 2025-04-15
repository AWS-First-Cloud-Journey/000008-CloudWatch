---
title: "CloudWatch Alarms"
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

#### Amazon CloudWatch Alarms

**ℹ️ Information**: CloudWatch Alarms monitor your metrics and trigger actions when thresholds are breached. They're essential for proactive monitoring and automated responses to changing conditions in your AWS environment.

Follow these steps to create an alarm for the error log metric we configured in the previous section:

1. Navigate to the CloudWatch console:

   - Select **Alarms** from the left navigation pane
   - Choose **All alarms**
   - Click **Create alarm**

![5.1](/images/5-cloud-watch-alarm/5.1.png)

2. Begin the metric selection process:

   - Click **Select metric**

![5.2](/images/5-cloud-watch-alarm/5.2.png)

   - Under **Custom namespaces**, select **ec2-logs**

![5.3](/images/5-cloud-watch-alarm/5.3.png)

   - Select **Metrics with no dimensions**
   - Choose **/var/log/messages - ERROR** metric
   - Click **Select metric**

![5.4](/images/5-cloud-watch-alarm/5.4.png)

3. Configure the metric parameters:

   - Set **Period** to **1 minute** for timely detection of error spikes

![5.5](/images/5-cloud-watch-alarm/5.5.png)

4. Define the alarm conditions:

   - Threshold type: **Static**
   - Condition: **Greater than 10**

![5.6](/images/5-cloud-watch-alarm/5.6.png)

**💡 Pro Tip**: The dashed line represents your threshold boundary. When the metric crosses this line, the alarm will transition to the ALARM state, indicating unusual application behavior that requires immediate investigation.

![5.7](/images/5-cloud-watch-alarm/5.7.png)

   - Click **Next** to continue

5. Configure notification settings:

   - Alarm state trigger: **In alarm**
   - Select **Create new topic**
   - Topic name: `Error_logs_reach_10`
   - Email to notify: enter your email address
   - Click **Create topic**

![5.8](/images/5-cloud-watch-alarm/5.8.png)

![5.9](/images/5-cloud-watch-alarm/5.9.png)

   - Click **Next**

![5.10](/images/5-cloud-watch-alarm/5.10.png)

6. Name your alarm:

   - Enter alarm name: `PythonApplicationErrorAlarm`
   - Click **Next**

![5.11](/images/5-cloud-watch-alarm/5.11.png)

7. Review and create:

   - Verify all configurations
   - Click **Create alarm**

![5.12](/images/5-cloud-watch-alarm/5.12.png)

![5.13](/images/5-cloud-watch-alarm/5.13.png)

**⚠️ Warning**: Your alarm will remain in the INSUFFICIENT_DATA state until Amazon SNS confirms your subscription and the metric receives data points.

![5.14](/images/5-cloud-watch-alarm/5.14.png)

8. Confirm your SNS subscription:

   - Check your email for a message from **AWS Notifications**

![5.15](/images/5-cloud-watch-alarm/5.15.png)

   - Click **Confirm subscription**

![5.16](/images/5-cloud-watch-alarm/5.16.png)

![5.17](/images/5-cloud-watch-alarm/5.17.png)

**🔒 Security Note**: Always confirm SNS subscriptions promptly to ensure you receive critical alerts. Consider using Amazon SNS with AWS Lambda for automated remediation of issues detected by CloudWatch Alarms.

Your CloudWatch Alarm is now fully configured and will monitor your application for error spikes, notifying you when the threshold is exceeded.
