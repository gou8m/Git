import pymysql
import os
client = boto3.client('ec2')
response = client.run_instances(
    ImageId='ami-00ca32bbc84273381',
    InstanceType='t2.micro',
    KeyName='Windows OS',
    MaxCount=3,
    MinCount=1,
)
