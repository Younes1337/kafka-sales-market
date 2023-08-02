# <p align="center"><span style="color:green">Kafka Sales Market realtime</span> 👋</p>


<p align="center">
    <a title="Apache Software Foundation, Apache License 2.0 <http://www.apache.org/licenses/LICENSE-2.0>, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Apache_kafka.svg">
        <img width="50" alt="Apache kafka" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Apache_kafka.svg/128px-Apache_kafka.svg.png">
    </a>
    <a title="Amazon.com Inc., Apache License 2.0 <http://www.apache.org/licenses/LICENSE-2.0>, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Amazon_Web_Services_Logo.svg">
        <img width="90" alt="Amazon Web Services Logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/512px-Amazon_Web_Services_Logo.svg.png">
    </a>
    <a href="https://cdnlogo.com/logo/python_358.html" ><img src="https://www.cdnlogo.com/logos/p/3/python.svg" width="50"></a>
</p>

Welcome to the **Kafka realtime sales market**! This project is a demonstration of setting up and running Apache Kafka on an AWS EC2 instance. It allows you to create a Kafka topic, produce messages, and consume messages using the Kafka console tools.

## Prerequisites 🛠️

- Java 1.8 or higher installed on your EC2 instance.
- Access to an AWS EC2 instance with public IP.
- Internet connectivity on the EC2 instance.

## Getting Started 🚀

Follow the steps below to set up and run Kafka on your AWS EC2 instance.

```bash
# Step 1: Download Kafka
wget https://downloads.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz
tar -xvf kafka_2.12-3.3.1.tgz
cd kafka_2.12-3.3.1
```

### Step 2: Install Java (if not already installed)
```bash
java -version
sudo yum install java-1.8.0-openjdk
java -version
```

### Step 3: Start ZooKeeper
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### Step 4: Start Kafka-server (In a new console)
```bash
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
bin/kafka-server-start.sh config/server.properties
```


### Step 5: Create a Kafka Topic
```bash
bin/kafka-topics.sh --create --topic demo_testing2 --bootstrap-server <public_ip>:9092 --replication-factor 1 --partitions 1
```
### Step 6: Start the Kafka Producer
```bash
bin/kafka-console-producer.sh --topic demo_testing2 --bootstrap-server <public_ip>:9092
```
### Step 7: Start the Kafka Consumer (In a new console)
```bash
bin/kafka-console-consumer.sh --topic demo_testing2 --bootstrap-server <public_ip>:9092
```
## Architecture 
<p align="center">
   <a><img src="Architecture.jpg"></a>
</p>

## Technology Used 🚀

- Programming Language: Python 🐍
- Amazon Web Services (AWS) ☁️

  - S3 (Simple Storage Service) 🗄️
  - Athena 📊
  - Glue Crawler 🐜
  - Glue Catalog 📑
  - EC2 💻

- Apache Kafka 🚀


