---
title: "CloudWatch Logs Insights"
weight: 2
chapter: false
pre: " <b> 4.2 </b> "
---

### CloudWatch Logs Insights

In this section, we will create logs from an application and then query these logs using **CloudWatch Logs Insights**. We’ll use an **EC2 instance** as an example.

1. In the service search bar:

   - Type ``EC2``.
   - Select **EC2**.

![4.2.1](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.1.png)

2. In the **EC2 Console**, go to the **Instances** page:

   - Select any instance (here we select `Instance-A`).
   - Click **Connect**.

![4.2.2](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.2.png)

3. On the **Connect to instance** page:

   - Switch to the **Session Manager** tab.
   - Click **Connect**.

![4.2.3](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.3.png)

4. Wait a few seconds, and a **Terminal** will appear:

   - Navigate to the `/tmp` directory.
   - Download the Python script from your S3 bucket:

```bash
cd /tmp
sudo aws s3 cp s3://<workshop-template-bucket>/logger.py .

```
   - Replace <workshop-template-bucket> with the name of the bucket you created in Section 2.


![4.2.4](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.4.png)

5. Grant execution permission and run the script:

```bash
sudo chmod +x logger.py
python3 logger.py &
```

![4.2.5](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.5.png)

6. Check the running logger processes:

```bash
ps -aux | grep logger
```

There are currently two processes running. They will keep running until the end of this lab.

![4.2.6](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.6.png)

7. Print log lines from `/var/log/messages`. This command will keep running until you stop it:

```bash
sudo tail -f /var/log/messages
```

![4.2.7](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.7.png)

8. Go back to the CloudWatch Console and open Logs Insights from the left menu.

![4.2.8](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.8.png)

9. In the **Selection criteria**, search for `/ec2` and select **/ec2/linux/var/log/messages**

![4.2.9](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.9.png)

10. Enter the following query and click Run query:

```
fields @timestamp, @message
| sort @timestamp desc
| limit 20
```

   - You should see a result similar to this:

![4.2.10](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.10.png)

   - These are the logs that were just generated.

![4.2.11](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.11.png)

11. Query logs containing ERROR:

```
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 20
```

![4.2.12](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.12.png)

   - These are the error logs we generated earlier.

![4.2.13](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.13.png)

12. Query logs containing WARN:

```
fields @timestamp, @message
| filter @message like /WARN/
| sort @timestamp desc
| limit 20
```

![4.2.14](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.14.png)

13. Re-run the error log query to see newly generated logs:

![4.2.15](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.15.png)

14. Query by another keyword (`eth0`):

```
fields @timestamp, @message
| filter @message like /eth0/
| sort @timestamp desc
| stats count (*) by bin()
```

![4.2.16](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.16.png)

![4.2.17](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.17.png)

### Visualizing Log Queries

You can view query results as charts by switching to the **Visualization** tab.

![4.2.18](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.18.png)

### Saving Queries

Logs Insights allows you to save queries for later use.

1. For example, to save the **ERROR** logs query:

- Go back to **Logs Insights**.

- Re-enter the **ERROR** logs query.

- Click **Save**.

![4.2.19](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.19.png)

2. In the **Save a new query** dialog, fill in the information:

- Query name: `Errors`.

- **Folder**: `cloudwatch-workshop` (create a new one if needed).

- Check the **Query definition details**.

- Click **Save**.

![4.2.20](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.20.png)

![4.2.21](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.21.png)

### Query History

Logs Insights provides a query history feature. You can view it by selecting **History** below the Query editor.

![4.2.22](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.22.png)

![4.2.23](/images/4-cloud-watch-logs/4.2-logs-insights/4.2.23.png)

n the next section, we will create a **Metrics Filter**, convert logs into **Metrics**, and set up an **Alarm**.
