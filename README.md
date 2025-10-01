# AWS CloudWatch Workshop

A comprehensive hands-on workshop for learning Amazon CloudWatch monitoring and observability capabilities.

## 🎯 Workshop Overview

This workshop provides practical experience with Amazon CloudWatch, AWS's comprehensive monitoring and management service. You'll learn to collect, analyze, and act on performance and operational data from AWS resources, applications, and services.

![CloudWatch Architecture](/static/images/architecture.png)

## 📚 What You'll Learn

- **CloudWatch Metrics**: Monitor and visualize AWS resource performance
- **CloudWatch Logs**: Centralize and analyze log data from applications and services
- **CloudWatch Alarms**: Set up automated notifications and actions based on metrics
- **CloudWatch Dashboards**: Create custom visualizations for operational insights
- **Advanced Features**: Search expressions, math expressions, and dynamic labels

## 🏗️ Workshop Structure

1. **[Introduction](content/1-introduction)** - CloudWatch fundamentals and use cases
2. **[Preparation Steps](content/2-preparatory-steps)** - Set up AWS resources for the workshop
3. **[CloudWatch Metrics](content/3-cloud-watch-metric)** - Working with metrics and visualizations
   - View Metrics
   - Search Expressions
   - Math Expressions
   - Dynamic Labels
4. **[CloudWatch Logs](content/4-cloud-watch-logs)** - Log management and analysis
   - Log Groups and Streams
   - CloudWatch Logs Insights
   - Metric Filters
5. **[CloudWatch Alarms](content/5-cloud-watch-alarm)** - Automated monitoring and alerting
6. **[CloudWatch Dashboard](content/6-cloud-watch-dashboard)** - Custom monitoring dashboards
7. **[Cleanup Resources](content/7-clean-up-resources)** - Remove workshop resources

## 🚀 Getting Started

### Prerequisites

- AWS Account with appropriate permissions
- Basic understanding of AWS services
- Familiarity with AWS Management Console

### Workshop Deployment

This workshop is built using Hugo static site generator with the Learn theme.

#### Local Development

1. **Install Hugo**
   - [Windows](https://gohugo.io/installation/windows/)
   - [Linux](https://gohugo.io/installation/linux/)
   - [macOS](https://gohugo.io/installation/macos/)

2. **Clone and Run**
   ```bash
   git clone https://github.com/AWS-First-Cloud-Journey/000008-CloudWatch.git
   cd 000008-CloudWatch
   hugo server -D
   ```

3. **Access Workshop**
   - Open browser to `http://localhost:1313`

#### Production Deployment

The workshop is automatically deployed via GitHub Actions when changes are pushed to the `main` branch.

## 🌟 Key Features

### CloudWatch Capabilities Covered

- **Unified Monitoring**: Single pane of glass for AWS resources
- **Real-time Metrics**: High-resolution data with 1-second granularity
- **Log Analytics**: Centralized logging with powerful query capabilities
- **Automated Actions**: Alarm-driven responses and notifications
- **Custom Dashboards**: Tailored visualizations for your environment
- **Container Insights**: Specialized monitoring for containerized applications

### Workshop Benefits

- **Hands-on Learning**: Practical exercises with real AWS resources
- **Best Practices**: Industry-standard monitoring approaches
- **Cost Optimization**: Learn to optimize resources using CloudWatch data
- **Troubleshooting**: Develop skills for identifying and resolving issues
- **Automation**: Implement automated monitoring and response workflows

## 🛠️ Technical Details

### Built With

- **Hugo**: Static site generator
- **Learn Theme**: Documentation-focused Hugo theme
- **GitHub Actions**: Automated deployment pipeline
- **AWS Services**: CloudWatch, EC2, Lambda, and more

### Supported Languages

- English (Primary)
- Vietnamese (Tiếng Việt)

### Browser Compatibility

- Modern browsers with JavaScript enabled
- Mobile-responsive design
- Progressive Web App features

## 📖 Workshop Content

### Metrics Deep Dive
Learn to work with CloudWatch metrics including:
- Built-in AWS service metrics
- Custom application metrics
- Composite metrics using math expressions
- Metric search and filtering

### Logs Management
Master CloudWatch Logs capabilities:
- Log group and stream organization
- Real-time log streaming
- Log retention policies
- Advanced querying with Logs Insights

### Alerting and Automation
Implement proactive monitoring:
- Threshold-based alarms
- Anomaly detection alarms
- Multi-metric alarms
- Integration with SNS and Lambda

### Visualization and Dashboards
Create compelling operational views:
- Custom dashboard creation
- Widget types and configurations
- Cross-region monitoring
- Sharing and permissions

## 🤝 Contributing

We welcome contributions to improve this workshop:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with Hugo
5. Submit a pull request

### Content Guidelines

- Follow existing structure and formatting
- Include practical examples
- Test all procedures
- Update both English and Vietnamese versions
- Optimize images for web delivery

## 📞 Support

- **AWS Study Group**: [Facebook Community](https://www.facebook.com/groups/awsstudygroupfcj/)
- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Documentation**: Refer to [AWS CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)

## 📄 License

This workshop is provided under the MIT License. See LICENSE file for details.

## 🏷️ Tags

`AWS` `CloudWatch` `Monitoring` `Observability` `DevOps` `Workshop` `Hands-on` `Tutorial`

---

## Cập nhật workshop

- Phần 2: Thêm các bước tạo S3 và upload file logger.py để phục vụ cho p3
- Thêm phần biểu thức còn thiếu trong ***mục 4 phần 3.2***
- Sửa lỗi biểu thức trong ***mục 4 phần 3,3***
- Ở **4.2** đã thêm note "sửa tên bucket" và thêm bản **Tiếng Anh**


**Note**: This workshop is designed for educational purposes. Always follow AWS best practices and your organization's security policies when implementing monitoring solutions in production environments.
