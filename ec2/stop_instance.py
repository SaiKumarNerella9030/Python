import boto3

instance_id = 'i-026fe1be0eae3ba0f'
ec2 = boto3.client('ec2')

response = ec2.stop_instances(InstanceIds=[instance_id])
print(f"Stopping instance: {instance_id}")
