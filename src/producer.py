import pandas as pd
from kafka import KafkaProducer, KafkaConsumer
from time import sleep
from json import dumps
import json
import argparse


def produce_data(EC2_IP_ADDRESS):
    # Create the Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=[f'{EC2_IP_ADDRESS}:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )

    if producer is not None:
        # Send the CSV data
        data = pd.read_csv('./notebooks/indexProcessed.csv')
        while True:
            dict_stock = data.sample(1).to_dict(orient="record")[0]
            producer.send("demo_testing2", value=dict_stock)
            sleep(1)

        # Clear data from the Kafka server
        producer.flush()

    else:
        print("An error has occurred. Try Again! (Check your EC2 public IP address)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Produce data to Kafka")
    parser.add_argument("--ec2-ip", help="EC2 public IP address", required=True)
    args = parser.parse_args()

    produce_data(args.ec2_ip)
