# ------------------------------------------------------------------------------
# Lambda Function to STOP/START EC2 Instances with specific TAG
#
# Version  Date          Name            Info
# 1.0      10-Dec-2022   Denis Astahov   Initial Version
#
# ------------------------------------------------------------------------------
import boto3
import os

EC2TAG_KEY    = os.environ["EC2TAG_KEY"]
EC2TAG_VALUE  = os.environ["EC2TAG_VALUE"]
EC2_ACTION    = os.environ["EC2_ACTION"]

ec2 = boto3.client('ec2')

def get_list_of_servers_with_tag(EC2TAG_KEY, EC2TAG_VALUE, EC2_ACTION):
    server_ids = []
    if EC2_ACTION == "STOP":
        instance_state_values = ["running"]
    if EC2_ACTION == "START":
        instance_state_values = ["stopped"]

    response = ec2.describe_instances(
        Filters=[
            {
             'Name'  : "tag:" + EC2TAG_KEY,
             'Values': [EC2TAG_VALUE]
            },
            {
             'Name'  : "instance-state-name",
             'Values': instance_state_values
            }
        ]
    )
    if len(response['Reservations']) > 0:
        for server in response['Reservations'][0]['Instances']:
            server_ids.append(server['InstanceId'])
    return server_ids



#-----------------START HERE----------------------------------------------------
def lambda_handler(event, context):
    try:
        server_ids = get_list_of_servers_with_tag(EC2TAG_KEY, EC2TAG_VALUE, EC2_ACTION)
        if len(server_ids) > 0:
            print("Servers to " + EC2_ACTION + ": " + str(server_ids))

            if EC2_ACTION == "STOP":
                ec2.stop_instances(InstanceIds=server_ids)
            if EC2_ACTION == "START":
                ec2.start_instances(InstanceIds=server_ids)
        else:
            print("No Servers to " + EC2_ACTION)

    except Exception as error:
        print("Error occuried! Error Message: " + str(error))

    return "DONE"
#-------------------------------------------------------------------------------
