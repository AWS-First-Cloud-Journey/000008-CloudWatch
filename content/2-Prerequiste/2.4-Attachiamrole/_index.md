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

![Attach IAM Role](/images/4/0001.png?featherlight=false&width=90pc)

1. In the **EC2** interface

- Select **Instances**
- Select the newly created instance

![Attach IAM Role](/images/4/0002.png?featherlight=false&width=90pc)

3. In the **EC2** interface

- Select **Actions**
- Select **Security**
- Select **Modify IAM role**

![Attach IAM Role](/images/4/0003.png?featherlight=false&width=90pc)

4. In the **Modify IAM role** interface

- Select **CloudWatchAgentRole**
- Select **Save**

![Attach IAM Role](/images/4/0004.png?featherlight=false&width=90pc)

5. Completed role assignment successfully

- Check the instance that has been assigned the IAM role

![Attach IAM Role](/images/4/0005.png?featherlight=false&width=90pc)