import boto3
from datetime import datetime, timedelta

profile = 'infinitelambda'
region = 'eu-west-1'
session = boto3.session.Session(profile_name=profile)

cloudwatch = boto3.client('cloudwatch')
rds_client = boto3.client("rds")
ec2_client = boto3.client('ec2')

paginator = cloudwatch.get_paginator('list_metrics')
metrics_list = []

for response in paginator.paginate(MetricName='CPUUtilization'):
    metrics_list = response['Metrics']

for item in metrics_list:
    instance_type = None

    if len(item.get("Dimensions")) > 0:

        if item.get("Namespace") == "AWS/RDS" and item.get("Dimensions")[0].get(
                "Name") == "DBInstanceIdentifier":
            #if item.get("Dimensions")[0].get("Value") != 'acloudguru':  # something is not right in the logic because acloudguru is not in any region
            rds_response = None
            try:
                rds_response = rds_client.describe_db_instances(
                    DBInstanceIdentifier=item.get("Dimensions")[0].get("Value"),
                )
            except:
                pass
            instance_type = rds_response.get("DBInstances")[0].get("DBInstanceClass")

        elif item.get("Namespace") == "AWS/EC2" and item.get("Dimensions")[0].get("Name") == "InstanceId":
            #if item.get("Dimensions")[0].get("Value") not in ["i-0db01ca8111c9bfb6", "i-079c667c182c64ba9"]: # something is not right in the logic because acloudguru is not in any region
            try:
                ec2_response = ec2_client.describe_instance_attribute(
                    Attribute='instanceType',
                    InstanceId=item.get("Dimensions")[0].get("Value")
                )
            except:
                pass

    if instance_type is not None:
        response = cloudwatch.get_metric_statistics(
            Namespace=item.get("Namespace"),
            MetricName='CPUUtilization',
            Dimensions=[
                {
                    'Name': item.get("Dimensions")[0].get("Name"),
                    'Value': item.get("Dimensions")[0].get("Value")
                },
            ],
            StartTime=datetime.utcnow() - timedelta(minutes=5),
            EndTime=datetime.utcnow(),
            Period=300,
            Statistics=['Average'],  # 'SampleCount','Average','Sum','Minimum','Maximum'
        )
        # calculate emission
        current_cpu_avg = response.get("Datapoints")[0].get("Average") if len(
            response.get("Datapoints")) > 0 else 0