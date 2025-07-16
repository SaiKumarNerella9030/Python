import boto3

ec2 = boto3.client('ec2')
instance_id = 'i-026fe1be0eae3ba0f'

ec2.create_tags(
    Resources=[instance_id],
    Tags=[
        {'Key': 'Environment', 'Value': 'Dev'},
        {'Key': 'Owner', 'Value': 'SaiKumar'}
    ]
)

print(f"Tags applied to {instance_id}")
