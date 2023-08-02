#!/bin/bash

# Provide the required credentials and arguments here
AWS_ACCESS_KEY_ID="<Your-AWS-ACCESS-KEY-ID>"
AWS_SECRET_ACCESS_KEY="<Your-AWS-SECRET-ACCESS-KEY>"
S3_BUCKET_NAME="<Your-S3-bucket-name>"
KAFKA_TOPIC="demo_testing2"
EC2_IP_ADDRESS="<Your-EC2-Public-IP-Address>"

# Execute the Python scripts with the command-line arguments
python store_data_to_s3.py --bucket $S3_BUCKET_NAME --topic $KAFKA_TOPIC --access-key $AWS_ACCESS_KEY_ID --secret-key $AWS_SECRET_ACCESS_KEY
python produce_data.py --ec2-ip $EC2_IP_ADDRESS
