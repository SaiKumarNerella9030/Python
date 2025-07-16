import boto3

ec2 = boto3.client('ec2')
regions = ec2.describe_regions()

print("Available AWS Regions:")
for region in regions['Regions']:
    print(region['RegionName'])
