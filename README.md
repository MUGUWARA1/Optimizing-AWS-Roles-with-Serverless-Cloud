

# AWS Serverless Role Optimizer

This project is a serverless solution built using AWS Lambda, S3, and the Boto3 library to identify IAM roles that lack "Permission Boundaries." It also includes a log monitoring system to detect access denial events, automatically managing them to enhance the security of the AWS environment.


## Description :
A serverless solution that identifies AWS IAM roles lacking "Permission Boundaries," stores the information in S3, and sends pre-signed URLs, with automated log monitoring for access denial management.

## Features

- Identifies IAM roles without "Permission Boundaries"
- Stores role details in S3 with pre-signed URL access
- Implements AWS Lambda for automated detection and management
- Includes a log monitoring system to track access denials
- Enhances security by automating responses to permission issues

## Tech Stack

- **AWS Lambda**: Serverless compute
- **S3**: Storage for role details
- **Boto3**: AWS SDK for Python to interact with AWS services
- **CloudWatch Logs**: Monitoring and logging of access denial events
- **Python**: Programming language
- **BOTO3 Library** 
- **AWS SNS**, **AWS SQS** : Send, store, and receive messages

## Usage

- The Lambda function will automatically scan for IAM roles missing "Permission Boundaries."
- The roles are stored in an S3 bucket, and pre-signed URLs are generated for secure access.
- CloudWatch Logs will monitor any access denials, and the system will automatically manage these events.

## Architecture Overview

![Serverless useCase1 jpg](https://github.com/user-attachments/assets/63791c37-08c8-4ab7-96c0-dedd74748ef0)


The system architecture consists of:
- AWS Lambda function for scanning IAM roles and handling access denial events
- S3 for storing the IAM role data
- CloudWatch for log monitoring and triggering actions


## Contributions

Contributions are welcome. Feel free to fork this repo, make improvements, or report issues.

