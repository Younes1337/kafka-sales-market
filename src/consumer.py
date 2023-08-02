from kafka import KafkaConsumer
from time import sleep 
from json import dump, loads
from s3fs import S3FileSystem
import json
import argparse

def store_data_to_s3(bucket_name, topic, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
    # Connect to your S3 Bucket 
    s3 = S3FileSystem(key=AWS_ACCESS_KEY_ID, secret=AWS_SECRET_ACCESS_KEY)

    for count , i in enumerate(consumer):
        filename = "stock_market_{}.json".format(count)

        message_val_str = str(i.value).replace("'", '"')
        message_val = json.loads(message_val_str)

        with s3.open("{}/{}".format(bucket_name, filename), 'w') as file:
            json.dump(message_val, file)

if __name__ == "__main__":
    #args section (credentials)
    parser = argparse.ArgumentParser(description="Store Kafka messages to S3")
    parser.add_argument("--bucket", help="S3 bucket name", required=True)
    parser.add_argument("--topic", help="Kafka topic", required=True)
    parser.add_argument("--access-key", help="AWS Access Key ID", required=True)
    parser.add_argument("--secret-key", help="AWS Secret Access Key", required=True)
    args = parser.parse_args()

    # Creating the consumer 
    consumer = KafkaConsumer(
        args.topic,
        bootstrap_servers=['<Your_EC2_public_ip_address>:9092'],
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

    store_data_to_s3(args.bucket, consumer, args.access_key, args.secret_key)
