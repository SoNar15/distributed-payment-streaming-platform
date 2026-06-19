# Distributed Real-Time Payment Streaming Platform

A distributed event-driven payment processing platform built using Apache Kafka, PySpark Structured Streaming, and Lakehouse architecture concepts.

---

## Architecture

```text
Payment Generator
        ↓
Kafka Producer
        ↓
Kafka Topic (payments)
        ↓
Spark Structured Streaming
        ↓
Bronze Layer (Next Phase)
        ↓
Silver Layer (Planned)
        ↓
Analytics Layer (Planned)
```

---

## Tech Stack

### Data Generation

* Python
* Faker

### Streaming

* Apache Kafka 3.8.1 (KRaft Mode)

### Processing

* PySpark 3.5.1
* Spark Structured Streaming

### Development Environment

* Windows 11
* WSL2 Ubuntu 24.04
* Git
* GitHub

### Future Enhancements

* Delta Lake
* Apache Airflow
* Docker
* AWS S3
* AWS Glue
* Athena

---

## Project Structure

```text
distributed-payment-streaming-platform/

├── generator/
│   └── payment_generator.py
│
├── streaming/
│   └── payment_producer.py
│
├── spark/
│   └── payment_stream_processor.py
│
├── docker/
│   └── docker-compose.yml
│
├── data/
│
├── docs/
│
├── screenshots/
│
├── venv/          (Windows Virtual Environment)
├── wsl_venv/      (WSL Virtual Environment)
│
├── requirements.txt
└── README.md
```

---

# Current Pipeline Implementation

## Step 1: Start Kafka Broker (Windows CMD)

Open Command Prompt.

Navigate to Kafka installation:

```cmd
cd E:\kafka\kafka_2.13-3.8.1
```

Start Kafka Broker:

```cmd
bin\windows\kafka-server-start.bat config\kraft\server.properties
```

Expected Output:

```text
Kafka Server started
Awaiting socket connections on 0.0.0.0:9092
```

Keep this terminal running.

---

## Step 2: Start Payment Generator (Windows Git Bash)

Open Git Bash.

Navigate to project:

```bash
cd /e/DE/distributed-payment-streaming-platform
```

Activate Windows virtual environment:

```bash
source venv/Scripts/activate
```

Run generator:

```bash
python generator/payment_generator.py
```

Expected Output:

```text
Sent to Kafka
Sent to Kafka
Sent to Kafka
...
```

This continuously generates synthetic payment transactions and publishes them to Kafka.

Keep this terminal running.

---

## Step 3: Start Spark Structured Streaming (WSL Ubuntu)

Open VS Code using WSL Ubuntu.

Navigate to project:

```bash
cd /mnt/e/DE/distributed-payment-streaming-platform
```

Activate WSL virtual environment:

```bash
source wsl_venv/bin/activate
```

Run Spark Streaming job:

```bash
python spark/payment_stream_processor.py
```

Expected Output:

```text
Creating Kafka stream...
Kafka stream created
Starting stream query...
Stream query started
Query active: True
```

Spark subscribes to the Kafka topic and processes payment events in real time.

---

## Current Working Data Flow

```text
Terminal 1 (Windows CMD)
Kafka Broker
        ↓

Terminal 2 (Windows Git Bash)
Payment Generator
        ↓

Kafka Topic: payments
        ↓

Terminal 3 (WSL Ubuntu)
Spark Structured Streaming
        ↓

Console Output
```

---

## Current Status

### Completed

* Kafka Broker Setup
* Kafka Producer
* Kafka Topic Creation
* Real-Time Payment Event Generation
* Spark Structured Streaming Setup
* Kafka-Spark Integration
* End-to-End Streaming Pipeline
* WSL-Based Spark Environment

### In Progress

* Bronze Layer (Parquet Storage)

### Planned

* Silver Layer Transformations
* Delta Lake Integration
* Airflow Orchestration
* Dockerized Deployment
* AWS S3 Data Lake
* AWS Glue Catalog
* Athena Analytics

---

## Goal

This project simulates a real-world financial event processing platform used in modern banking and payment infrastructure.

The objective is to demonstrate end-to-end Data Engineering concepts including event streaming, distributed processing, data lake architecture, workflow orchestration, and cloud integration.
