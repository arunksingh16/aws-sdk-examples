# aws-sdk-examples


Create a low-level service client by name using the default session:
```
boto3.client(*args, **kwargs)[source]
```

Create a resource service client by name using the default session:
```
boto3.resource(*args, **kwargs)[source]
```


To use boto3 with AWS Profile:
```
# Create a new session with the profile
session = boto3.Session(profile_name='dev')
region = os.environ['AWS_REGION']
ec2_client = session.client('ec2', region_name = region)
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

# Change the profile of the default session in code
boto3.setup_default_session(profile_name='dev')

```


Ref:
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/boto3.html


