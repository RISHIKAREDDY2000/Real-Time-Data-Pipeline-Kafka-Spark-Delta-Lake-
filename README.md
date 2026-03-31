# Real-Time Data Pipeline (Kafka + Spark + Delta Lake)

## Overview

This project implements a real-time financial transaction processing pipeline using Kafka, Apache Spark Structured Streaming, and Delta Lake.

The pipeline simulates streaming credit card transactions, processes them in real-time, applies fraud detection rules, and stores results in Delta Lake for analytics.

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

Dataset

The full dataset contains over 1 million financial transactions used to simulate a real-time fraud detection pipeline.

Due to GitHub storage limits, only a small sample dataset is included in this repository.

The pipeline architecture simulates streaming ingestion through Kafka and processing with Spark Structured Streaming.
