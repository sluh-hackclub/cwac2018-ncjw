import boto3

wasabi = boto3.client(
    's3',
    aws_access_key_id="3HOKH0H0TVT03XTYKWS9",
    aws_secret_access_key="gRfHaK68ObCIfYUzePgIz47SLGNjru0iwfzVbvMG",
)

wasabi.upload_file('example.txt', 'letters', '58924/example.txt')
