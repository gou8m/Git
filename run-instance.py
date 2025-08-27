import boto3
client = boto3.client('ec2')
response = client.run_instances(
    ImageId='ami-00ca32bbc84273381',
    InstanceType='t2.micro',
    KeyName='vaultaccess',
    MaxCount=1,
    MinCount=1,
)
