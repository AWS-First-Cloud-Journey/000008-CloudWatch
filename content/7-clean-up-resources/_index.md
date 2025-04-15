---
title: "Clean up resources"
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

#### Resource Cleanup

**ℹ️ Information**: Properly cleaning up AWS resources after completing this workshop prevents unexpected charges on your AWS account while allowing you to retain valuable monitoring data for future reference.

Follow these steps to remove all workshop resources:

1. Navigate to AWS CloudFormation:

   - In the AWS Management Console search bar, type `CloudFormation`
   - Select **CloudFormation** from the results

![7.1](/images/7-clean-up-resources/7.1.png)

2. Delete the CloudFormation stack:

   - Select the stack you created for this workshop
   - Click **Delete** to initiate the deletion process

![7.2](/images/7-clean-up-resources/7.2.png)

3. Confirm the deletion:

   - Review the resources that will be deleted
   - Click **Delete** to confirm

![7.3](/images/7-clean-up-resources/7.3.png)

**💡 Pro Tip**: CloudFormation handles the deletion of all resources in the correct order, ensuring proper cleanup without manual intervention.

4. Monitor the deletion process:

   - The stack status will change to "DELETE_IN_PROGRESS"
   - Wait for the stack to be completely removed from the list

![7.4](/images/7-clean-up-resources/7.4.png)

**⚠️ Warning**: While the infrastructure resources will be deleted immediately, CloudWatch Metrics and Logs data will remain available for up to 15 months according to the default retention policy, which may incur minimal storage costs.

**🔒 Security Note**: Consider reviewing your CloudWatch Logs retention policies for production environments to balance compliance requirements with cost optimization.
