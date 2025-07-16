import boto3
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')
instance_id = 'i-026fe1be0eae3ba0f'

end = datetime.utcnow()
start = end - timedelta(hours=1)

response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
    StartTime=start,
    EndTime=end,
    Period=300,
    Statistics=['Average']
)

for data in response['Datapoints']:
    print(f"Time: {data['Timestamp']} | Avg CPU: {data['Average']:.2f}%")
