import boto3
import json

# Vars
sg_name = 'rds-sg-dev-demo-bk'
sg_description = 'RDS SG for demo'
ip_cidr = '0.0.0.0/0'

# Create ec2 instance
ec2_client = boto3.client('ec2')

res = ec2_client.create_security_group(
    Description=sg_description,
    GroupName=sg_name)

print(json.dumps(res, indent=2, sort_keys=True))

# SG rule
res = ec2_client.authorize_security_group_ingress(
    CidrIp=ip_cidr,
    FromPort=3306,
    GroupName=sg_name,
    ToPort=3306,
    IpProtocol='tcp'
)
print('SG has been created check console...')
