---
title: "Preparatory steps"
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

#### Preparation Steps

**ℹ️ Information**: In this section, you'll set up the necessary AWS resources for the CloudWatch workshop using AWS CloudFormation. This automated deployment will create EC2 instances with pre-configured applications that generate metrics and logs for our monitoring exercises.

1. Access the **AWS Management Console**:

   - In the search bar, type **CloudFormation**.
   - Select **CloudFormation** from the services list.

![2.1](/images/2-preparatory-steops/2.1.png)

2. In the **CloudFormation** console:

   - Click **Create stack**.
   - Select **With new resources (standard)** from the dropdown.

![2.2](/images/2-preparatory-steops/2.2.png)

3. For the stack template:

   - Download the [CloudFormation template](https://raw.githubusercontent.com/AWS-First-Cloud-Journey/CloudWatchWorkshop/main/template.yml).
   - Under **Prerequisite - Prepare template**, select **Choose an existing template**.
   - Choose **Upload a template file**.
   - Click **Choose file** and select the template you just downloaded.
   - Click **Next** to proceed.

![2.3](/images/2-preparatory-steops/2.3.png)

4. Configure stack details:

   - Stack name: Enter `FCJ-CloudWatch-Workshop` (or a preferred name that's easily identifiable).
   - RegionId: Select the AWS Region where you're conducting this lab (for this example, we're using **us-east-1** - N. Virginia).
   - Keep all other parameters at their default values.
   - Click **Next**.

![2.4](/images/2-preparatory-steops/2.4.png)

**💡 Pro Tip**: Using a consistent naming convention for your CloudFormation stacks makes resource management easier, especially when working across multiple projects or environments.

5. Configure stack options:

   - No additional configuration is required on this page.
   - Scroll to the bottom and check the acknowledgment box: **I acknowledge that AWS CloudFormation might create IAM resources with custom names**.
   - Click **Next**.

![2.5](/images/2-preparatory-steops/2.5.png)

**🔒 Security Note**: The CloudFormation template creates IAM roles with least-privilege permissions necessary for this workshop. In production environments, always review IAM permissions carefully to ensure they follow security best practices.

6. Review and create:

   - Verify all configuration details.
   - Scroll to the bottom and click **Submit** to initiate stack creation.

![2.6](/images/2-preparatory-steops/2.6.png)

7. Monitor stack creation:

   - The stack creation process will begin immediately.
   - Wait approximately 5 minutes for the deployment to complete.
   - You can monitor the progress in the CloudFormation console.

![2.7](/images/2-preparatory-steops/2.7.png)

When the deployment completes successfully, you'll see the stack status change to **CREATE_COMPLETE**:

![2.8](/images/2-preparatory-steops/2.8.png)

**ℹ️ Information**: The CloudFormation stack has deployed EC2 instances running sample applications that will generate metrics and logs for our CloudWatch exercises. These resources are pre-configured to demonstrate various CloudWatch capabilities throughout this workshop.

#### Create an S3 Bucket and Upload the `logger.py` File

1. Search for **S3** in the AWS search bar.

   ![2.9](/images/2-preparatory-steops/2.9.png)

2. Click **Create bucket**.

3. The bucket name must be ***unique globally***. It cannot be duplicated.

   ![2.10](/images/2-preparatory-steops/2.10.png)

4. Leave all settings as their default values.

5. Scroll to the bottom of the page and click **Create bucket**.

   ![2.11](/images/2-preparatory-steops/2.11.png)

6. Select the bucket you just created.

7. Click **Upload** and upload the `logger.py` file to the bucket.

8. Verify that the file has been successfully uploaded.

   ![2.12](/images/2-preparatory-steops/2.12.png)


The preparation step is now complete. In the following sections, we'll explore CloudWatch's monitoring and observability features using the resources we've just deployed.
