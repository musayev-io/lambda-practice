import boto3
from datetime import datetime

region_name = 'us-east-1'

ec2 = boto3.resource('ec2', region_name=region_name)


def lambda_handler(event, context):
    # Iterate for all Instances within the Region
    for instance in ec2.instances.all():
        # Iterate for all Block Devices`
        for block_device in instance.block_device_mappings:
            # Skip if device is not EBS
            if block_device.get('Ebs') is None:
                continue
            volume_id = block_device.get('Ebs').get('VolumeId')
            # Assume all other devices are EBS
            # Iterate through tags and look for backups
            for tag in instance.tags:
                if tag['Key'] == "Backup" and tag['Value'] == "Yes":
                    current_date = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
                    snapshot_description = instance.instance_id + "_" + current_date
                    # Create EBS Snapshot
                    ec2.create_snapshot(
                        VolumeId=volume_id,
                        Description=snapshot_description
                    )
