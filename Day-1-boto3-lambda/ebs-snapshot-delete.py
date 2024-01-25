import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    
    snapshot_response = ec2.describe_snapshots(OwnerIds=["self"])
    
    
    instance_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    active_instance_ids = set()
    
    for reservation in instance_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    for snapshot in snapshot_response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

