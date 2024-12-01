from google.cloud import storage

client = storage.Client()
bucket = client.bucket("pangotalk-bucket")
blob = bucket.blob("test.txt")

blob.upload_from_string("Hello, world!")
print(f"File uploaded to: {blob.public_url}")
