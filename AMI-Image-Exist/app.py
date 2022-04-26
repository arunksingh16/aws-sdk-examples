import json
import boto3
from botocore.exceptions import ClientError
import logging


session = boto3.Session(profile_name='myprofile')

region = os.environ['AWS_REGION']

ec2_client = session.client('ec2', region_name = region)

# EC2_RESOURCE = boto3.resource('ec2', region_name=region)
# images = EC2_RESOURCE.images.all()
# for image in images:
#     print(f'AMI {image.id}: {image.name}')

newAmiID="ami-xxxxxxxx"

# When you make an API call, whether it is a GET, PUSH or PUT, you will get a response. 
# The response is in a structured format, using Keys and Values. In Python, that';s a dictionary (dict).


def check_image_exists(newAmiID, region): 
    response = ec2_client.describe_images(ImageIds=[newAmiID,])
    # Convert Python Dictionary To JSON
    json_object = json.dumps(response, indent = 4) 
    print(json_object)
    print(response['ResponseMetadata']['HTTPStatusCode'])
    for image in response['Images']:
      if newAmiID == image['ImageId']:
        return True
    return False

def test():
    check_status = check_image_exists(newAmiID, region)
    if not check_status:
        return(print("No AMI id found for region {}".format(region)))
    else:
        return(print("Image exists"))

if __name__ == '__main__':
    test()
