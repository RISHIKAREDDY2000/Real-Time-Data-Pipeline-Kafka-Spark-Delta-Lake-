# Real-Time Data Pipeline

Kafka + Spark Structured Streaming + Delta Lake

## Overview

This project demonstrates a real-time data engineering pipeline that processes financial transaction data using Apache Kafka and Spark Structured Streaming. The pipeline ingests streaming transaction events, applies transformations, and stores the results in Delta Lake for analytics.

The goal of this project is to simulate a modern streaming data platform used for processing high-volume event data.

## Architecture

Transaction Generator
→ Apache Kafka
→ Spark Structured Streaming
→ Delta Lake
→ Analytics / BI Tools

## Tech Stack

Apache Kafka
Apache Spark
Delta Lake
Python
SQL

## Pipeline Workflow

1. Transaction data is generated and sent to a Kafka topic.
2. Spark Structured Streaming reads streaming data from Kafka.
3. Transformation logic flags high-value transactions.
4. Processed data is stored in Delta Lake tables.

## Use Cases

Fraud detection systems
Real-time financial analytics
Streaming event processing
