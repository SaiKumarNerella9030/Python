import boto3

instance_ids = ['i-026fe1be0eae3ba0f']  # Add one or more instance IDs

ec2 = boto3.client('ec2')

response = ec2.terminate_instances(InstanceIds=instance_ids)

for instance in response['TerminatingInstances']:
    print(f"Instance ID: {instance['InstanceId']}")
    print(f"Previous state: {instance['PreviousState']['Name']}")
    print(f"Current state: {instance['CurrentState']['Name']}")
