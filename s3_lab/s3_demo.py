import boto3

s3 = boto3.client("s3")

def create_bucket(bucket_name):
    s3.create_bucket(Bucket=bucket_name)
    print("Bucket created:", bucket_name)

def list_buckets():
    response = s3.list_buckets()
    print("Existing buckets:")
    for bucket in response["Buckets"]:
        print(bucket["Name"])

if __name__ == "__main__":
    bucket_name = "john-2026-bucket-123"
    create_bucket(bucket_name)
    list_buckets()