from kafka import KafkaProducer
import pandas as pd
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

data = pd.read_csv('../datasets/transactions_sample.csv')

for index, row in data.iterrows():
    message = row.to_dict()
    producer.send('transactions_topic', value=message)
    print("Sent:", message)
    time.sleep(1)

producer.flush()
