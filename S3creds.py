import boto3
import os
client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key'),
    aws_session_token=None
)


#'AKIA6EGID2AGDMW2IKNU'
#'/vWrXXVa1bej85bEWlbZfJyxArWxMc/4cZXmlOC1',