---
title : "Introduction"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 1. </b> "
---

#### Amazon CloudWatch
Amazon CloudWatch is a tool that allows you to collect data about the performance of the resources, applications, and services running on the AWS Cloud or your servers. Collected data will be saved as logs, metrics, and events. Cloudwatch can also present data in the form of graphs for you to easily visualize and distill information from the data.

#### CloudWatch Agent
CloudWatch Agent is an application of the CloudWatch service. You need to download and launch the CloudWatch Agent on your on-premises server or EC2 Instance so that CloudWatch can collect activity data for each machine.

In this section, you will practice setting up CloudWatch Agent to monitor EC2 Instance's RAM and send data back to CloudWatch. In order for EC2 Instance to have access to CloudWatch, you need to assign it an appropriate IAM Role.

![CloudWatch](/images/architect.png)