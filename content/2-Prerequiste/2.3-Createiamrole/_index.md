---
title : "Create IAM role"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 2.3 </b> "
---

#### Create an IAM role
In this section, you will practice setting up CloudWatch Agent to monitor EC2 Instance's RAM and send data back to CloudWatch. For EC2 Instance to have access to CloudWatch, you need to assign it an appropriate IAM Role.

1. Go to [AWS Management Console](https://aws.amazon.com/console/)

- Find **IAM**
- Select **IAM**

![CreateIAMrole](/images/3/0001.png?featherlight=false&width=90pc)

2. In the **IAM** interface

- Select **Roles**
- Select **Create role**

![CreateIAMrole](/images/3/0002.png?featherlight=false&width=90pc)

3. In the **Select trusted entity** interface

- Select **AWS service**
- **Use case**, select **EC2**

![CreateIAMrole](/images/3/0003.png?featherlight=false&width=90pc)

4. In the **Add permissions** interface

- Search **CloudWatchAgentServer** policy
- Select **CloudWatchAgentServer** policy
- Select **Next**

![CreateIAMrole](/images/3/0004.png?featherlight=false&width=90pc)

5. In the **Role details** section

- Select **CloudWatchAgentRole**

![CreateIAMrole](/images/3/0005.png?featherlight=false&width=90pc)

6. Select **Create role**

![CreateIAMrole](/images/3/0006.png?featherlight=false&width=90pc)

7. Complete role creation

![CreateIAMrole](/images/3/0007.png?featherlight=false&width=90pc)