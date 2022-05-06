---
title : "Assign IAM role"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 2.4 </b> "
---

#### Assign IAM role
1. Go to [AWS Management Console](https://aws.amazon.com/console/)

- Find **EC2**
- Select **EC2**

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0001-attachiamrole.png)

2. In the **EC2** interface

- Select **Instances**
- Select the newly created instance

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0002-attachiamrole.png)

3. In **EC2** interface

- Select **Actions**
- Select **Security**
- Select **Modify IAM role**

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0003-attachiamrole.png)

4. In the **Modify IAM role** interface

- Select **CloudWatchAgentRole**
- Select **Save**

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0004-attachiamrole.png)

5. Completed role assignment successfully

- Check that the instance has been assigned the IAM role

![Attach IAM Role](/images/2-Prerequiste/2.3-Attachiamrole/0005-attachiamrole.png)