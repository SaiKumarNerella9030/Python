import boto3

sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:ap-south-1:123456789012:DevOpsAlerts'

message = 'EC2 instance i-12345678 has high CPU usage.'
subject = 'DevOps Alert: High CPU Usage'

sns.publish(
    TopicArn=topic_arn,
    Subject=subject,
    Message=message
)

print("Alert sent via SNS.")
