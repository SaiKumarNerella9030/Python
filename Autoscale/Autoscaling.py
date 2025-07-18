import boto3

asg = boto3.client('autoscaling')
asg_name = 'devops-asg'

asg.update_auto_scaling_group(
    AutoScalingGroupName=asg_name,
    DesiredCapacity=3
)

print(f"Auto Scaling Group '{asg_name}' scaled to 3 instances.")
