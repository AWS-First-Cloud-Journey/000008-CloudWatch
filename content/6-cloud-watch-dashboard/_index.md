---
title: "CloudWatch Dashboards"
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

#### Amazon CloudWatch Dashboards

**ℹ️ Information**: CloudWatch Dashboards provide a customizable home page in the CloudWatch console that you can use to monitor your resources across multiple regions. Dashboards allow you to create a unified view of the metrics and alarms that matter most to your operations.

In this final section of the workshop, we'll create a comprehensive dashboard to visualize the metrics and alarms we've configured throughout the previous modules, with special focus on the error log monitoring we established.

1. Add the alarm we created to the dashboard:

   - Select **PythonApplicationErrorAlarm**
   - Expand **Actions**
   - Select **Add to dashboard**

![6.1](/images/6-cloud-watch-dashboard/6.1.png)

2. In the **Add to dashboard** dialog:

   - Select **Create new**

![6.2](/images/6-cloud-watch-dashboard/6.2.png)

3. Configure your new dashboard:

   - Enter dashboard name: `CloudWatch-Workshop`
   - Click **Create**
   - Click **Add to dashboard**

![6.3](/images/6-cloud-watch-dashboard/6.3.png)

![6.4](/images/6-cloud-watch-dashboard/6.4.png)

**💡 Pro Tip**: Dashboards support cross-region monitoring, allowing you to track resources deployed across your global AWS infrastructure from a single view.

Your completed dashboard should now display the alarm widget:

![6.5](/images/6-cloud-watch-dashboard/6.5.png)

**ℹ️ Information**: Dashboard widgets are highly customizable. You can:

- Resize and reposition widgets by dragging
- Edit widget properties to change visualization types
- Add text annotations for context
- Share dashboards with your team

![6.6](/images/6-cloud-watch-dashboard/6.6.png)

![6.7](/images/6-cloud-watch-dashboard/6.7.png)

**🔒 Security Note**: Consider using AWS Identity and Access Management (IAM) to control who can view or modify your dashboards, especially when they contain sensitive operational metrics.

Congratulations on completing this workshop! You've successfully implemented a comprehensive monitoring solution using Amazon CloudWatch's powerful features for metrics, logs, alarms, and dashboards.
