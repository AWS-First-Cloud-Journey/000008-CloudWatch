---
title : "Create IAM role"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 2.3 </b> "
---

#### Create IAM role
In this section, you will practice setting up CloudWatch Agent to monitor EC2 Instance's RAM and send data back to CloudWatch. In order for EC2 Instance to have access to CloudWatch, you need to assign it an appropriate IAM Role.

1. Go to [AWS Management Console](https://aws.amazon.com/console/)

- Find **IAM**
- Select **IAM**

![CreateIAMrole](/images/2-Prerequiste/2.2-Createiamrole/0001-createiamrole.png)

2. In the **IAM** interface

- Select **Roles**
- Select **Create role**

![CreateIAMrole](/images/2-Prerequiste/2.2-Createiamrole/0002-createiamrole.png)

3. In the **Select trusted entity** interface

- Select **AWS service**
- **Use case**, select **EC2**

![CreateIAMrole](/images/2-Prerequiste/2.2-Createiamrole/0003-createiamrole.png)

4. In the **Add permissions** interface

- Search **CloudWatchAgentServer** policy
- Select **CloudWatchAgentServer** policy
- Select **Next**

![CreateIAMrole](/images/2-Prerequiste/2.2-Createiamrole/0004-createiamrole.png)

5. In the **Role details** section

- Select **CloudWatchAgentRole**

![CreateIAMrole](/images/2-Prerequiste/2.2-Createiamrole/0005-createiamrole.png)

6. Select **Create role**

![CreateIAMrole](/images/2-Prerequiste/2.2-Createiamrole/0006-createiamrole.png)

7. Complete role creation

![CreateIAMrole](/images/2-Prerequiste/2.2-Createiamrole/0007-createiamrole.png)