import boto3

ec2 = boto3.client('ec2')
instance_id = 'i-0abcdef1234567890'
iam_role = 'EC2S3AccessRole'

response = ec2.associate_iam_instance_profile(
    IamInstanceProfile={'Name': iam_role},
    InstanceId=instance_id
)

print(f"IAM role {iam_role} attached to instance {instance_id}")
