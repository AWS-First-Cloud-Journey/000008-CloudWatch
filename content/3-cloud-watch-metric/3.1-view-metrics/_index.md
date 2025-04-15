---
title: "Viewing Metrics"
weight: 1
chapter: false
pre: " <b> 3.1 </b> "
---

#### Viewing CloudWatch Metrics

**ℹ️ Information**: In this section, you'll learn how to navigate and visualize Amazon CloudWatch metrics to gain insights into your AWS resources' performance and health.

#### Accessing CloudWatch Metrics

1. Access the **AWS Management Console**:
   - In the search bar, type **CloudWatch**.
   - Select **CloudWatch** from the services list.

![3.1.1](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.1.png)

2. In the **CloudWatch** console:
   - Expand the **Metrics** section in the left navigation pane.
   - Select **All metrics**.

![3.1.2](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.2.png)

#### Finding EC2 Instance Metrics

1. In the metrics dashboard:
   - Enter `EC2` in the search bar to filter metrics by service.

![3.1.3](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.3.png)

2. From the search results:
   - Select **EC2 > Per-Instance Metrics** to view metrics for individual EC2 instances.

![3.1.4](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.4.png)

![3.1.5](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.5.png)

#### Analyzing CPU Utilization

1. Filter for specific metrics:
   - In the search bar, type `CPUUtilization` and press Enter.
   - By default, CloudWatch searches by **Metric name**.

![3.1.6](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.6.png)

![3.1.7](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.7.png)

2. Compare instance performance:
   - Select two of the five instances created by the CloudFormation stack.
   - Scroll down to view the graphed data.

**💡 Pro Tip**: When comparing multiple instances, look for patterns that might indicate system-wide events versus instance-specific issues.

3. Analyze the graph data:
   - Both instances initiated operations around **2:40 AM**, showing peak activity at this time.
   - By **3:30 AM**, both instances appear to have completed their workloads.

![3.1.8](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.8.png)

#### Examining Multiple Metrics

1. Focus on a single instance:
   - Deselect the line for **Instance B**.
   - Clear the **CPUUtilization** filter.
   - Search for `EBSWriteBytes` to examine storage I/O.

![3.1.9](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.9.png)

![3.1.10](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.10.png)

2. Select **Instance A** and analyze the correlation:
   - Initially, high volume of EBS read/write operations indicates data processing.
   - **CPUUtilization** and **EBSWriteBytes** follow similar patterns with some divergence.
   - This suggests the application primarily interacts with EBS during startup before transitioning to other operations.

![3.1.11](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.11.png)

3. For clearer analysis:
   - You can hide individual metrics by toggling their visibility.

![3.1.12](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.12.png)

**ℹ️ Information**: In the next section, we'll explore more advanced visualization techniques for better metric analysis.

#### Enhancing Chart Visualization

When multiple metrics with different units are displayed on the same chart, interpretation can be challenging. Let's improve visualization with CloudWatch's advanced charting features.

1. Separate Y-axis for different metrics:
   - Navigate to the **Graphed metrics** tab.
   - For **EBSWriteBytes**, click the **Y-axis** column dropdown and select **Right Y-axis**.
   - The chart now displays each metric on its appropriate scale.

![3.1.13](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.13.png)

2. Add a horizontal threshold annotation:
   - Go to the **Options** tab.
   - Click **Add horizontal annotation**.

![3.1.14](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.14.png)

3. Configure the threshold:
   - **Label**: `5% Mark`
   - **Value**: `5`
   - This adds a dashed horizontal line at the 5% CPU utilization level.

![3.1.15](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.15.png)

**💡 Pro Tip**: Horizontal annotations are excellent for visualizing thresholds that might trigger alarms or indicate performance boundaries.

4. Add a vertical event marker:
   - Create a **Vertical annotation** labeled `Job start`.
   - This adds a dashed vertical line to mark a specific point in time.

![3.1.16](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.16.png)

5. Adjust the vertical annotation time:
   - Hover over the **Job start** marker.
   - Note that the job actually started around **2:40 AM**.

![3.1.17](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.17.png)

6. Update the annotation:
   - Change the **Date/Time** for `Job start` to **2:40 AM**.
   - Click **Apply** to save your changes.

![3.1.18](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.18.png)

7. Verify the repositioned marker:
   - The `Job start` marker now aligns with the beginning of instance activity.

![3.1.19](/images/3-cloud-watch-metric/3.1-view-metrics/3.1.19.png)

**🔒 Security Note**: When analyzing metrics for production workloads, pay special attention to unexpected spikes or patterns that might indicate security events or unauthorized access.

#### Next Steps

This concludes our exploration of basic CloudWatch metric visualization. In the next section, we'll dive into **working with metric expressions** for more advanced analysis capabilities.

**⚠️ Warning**: Before proceeding to the next section, you may want to remove the annotations to start with a clean workspace.
