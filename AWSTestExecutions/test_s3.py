import boto3
from AWSTestCases.AWS_IAM_Test import aws_iam_check_if_policy_exist, aws_iam_check_if_role_exist

#create IAM client
s3 = boto3.client('s3')

def test_aws_s3_check_if_bucket_exist():
    assert aws_s3_check_if_bucket_exist(s3) == True
