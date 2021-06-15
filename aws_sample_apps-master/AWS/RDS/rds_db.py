import boto3
import json

# Vars
sg_name = 'sg-03507e7c60d2e8f76'
rds_id = ''
db_name = ''
user_name = ''
user_passwd = ''
admin_email = ''
sg_id_num = ''
rds_endpoint = ''


# 
ec2_client = boto3.client('ec2')

res = ec2_client.describe_security_groups(
    GroupsNames = [sg_name]
)

sg_id_num = json.dumps(res['SecurityGroups'][0]['GroupId'])
sg_id_num = sg_id_num.replace('"','')

# RDS Client
rds_client = boto3.client('rds')
# RDS Setup
res = rds_client.create_dn_instances(
    DBInstanceIdentifier=rds_id,
    DBName=db_name,
    Engine='mariadb',
    MasterUserName='masteruser',
    MasterUserPassword='mymasterpassw0rd1!',
    VpcSecurityGroupsIds=[
        sg_id_num
    ],
    AllocatedStorage=20,
    Tags=[{
        'Key': 'POC-Email',
        'Value': admin_email
    },
    {
        'Key': 'Purpose',
        'value': 'RDS demo app'
    }
    ]
)

#   Create DB
print('Creating the RDS Instace, this can take a few minutes...')
waiter = rds_client.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=rds_id)
print('Ok, you Amazon RDS is ready now!')