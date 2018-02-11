import boto3

client = boto3.client(
    's3',
    aws_access_key_id="3HOKH0H0TVT03XTYKWS9",
    aws_secret_access_key="gRfHaK68ObCIfYUzePgIz47SLGNjru0iwfzVbvMG",
)

response = client.list_buckets()

buckets = [bucket['Name'] for bucket in response['Buckets']]

print("Bucket List: %s" % buckets)
