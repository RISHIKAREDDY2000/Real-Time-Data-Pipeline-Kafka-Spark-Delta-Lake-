# Real-Time Data Pipeline (Kafka + Spark + Delta Lake)

## Overview

This project demonstrates a real-time data engineering pipeline that processes financial transactions.

The system streams transaction data through Kafka, processes it with Spark Structured Streaming, and stores the results in Delta Lake for analytics.

Pipeline Flow

Data Generator → Kafka → Spark Streaming → Delta Lake → Analytics

## Architecture

Data Generator → Kafka → Spark Structured Streaming → Delta Lake → BI Tools

## Technologies

Kafka
Apache Spark
Delta Lake
Python
Docker
Power BI

## Dataset

The project uses a simulated financial transaction dataset with over 1 million transactions.

Dataset includes:

transaction_id
client_id
card_id
merchant_id
amount
merchant_city
merchant_state
MCC code

Only a sample dataset is included in this repository.

## Key Features

Real-time streaming pipeline
Kafka event ingestion
Spark Structured Streaming transformations
Fraud detection rule engine
Delta Lake storage layer
Analytics ready data

## Running the Pipeline

Step 1
Start Kafka
Step 2
Run producer
Step 3
Run Spark streaming job

The full dataset contains 1M+ transactions used to simulate real-time streaming.
Only a small sample is included in the repository.
