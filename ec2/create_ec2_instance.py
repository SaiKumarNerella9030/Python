import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Change region as needed

# Launch EC2 instance
response = ec2.run_instances(
    ImageId='ami-0c02fb55956c7d316',       # Amazon Linux 2 AMI (example, us-east-1)
    InstanceType='t2.micro',               # Free tier eligible
    KeyName='us-east',                 # Replace with your key pair name
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=['sg-08fa173c3613'],
    SubnetId='subnet-07ac649a8164',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'MyBoto3Instance'}]
        }
    ]
)

# Print instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 Instance launched with ID: {instance_id}")
