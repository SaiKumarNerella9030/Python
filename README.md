# 🛠️ Boto3 DevOps Automation Scripts

A collection of real-world Python scripts using **Boto3** to automate common **AWS DevOps tasks**, organized from **basic to advanced**.

---

## 📦 Features

✅ List EC2 instances & manage them  
✅ Upload/download files to S3  
✅ Tag resources (EC2, S3)  
✅ Monitor EC2 CPU with CloudWatch  
✅ IAM user audits  
✅ Delete unused EBS volumes  
✅ Automate DNS, RDS snapshots, CloudFormation  
✅ Send alerts via SNS  
✅ Supports logging, error handling

---

## 📋 Prerequisites

- Python 3.7+
- `boto3` library installed
- AWS CLI configured with credentials

```bash
pip install boto3
aws configure
````


## 🔄 How to Use

```bash
python scripts/<script_name>.py
```

Make sure to update any hardcoded values like:

* `Instance ID`
* `Bucket Name`
* `Region`
* `File Paths`
  in each script before running.

---

---

## 📌 Best Practices Followed

* Modular and readable scripts
* Boto3 best practices for retries & exception handling
* Designed for DevOps engineers using AWS CLI & Python
* Easily extendable to Lambda, Step Functions, or CRON jobs

---

## 🔐 Security Note

> Avoid hardcoding AWS credentials in scripts. Use environment variables or `aws configure`.

