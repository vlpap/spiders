#!/usr/bin/env python
from kafka import KafkaConsumer
consumer = KafkaConsumer('theIS',bootstrap_servers='10.93.221.39:9092')
for msg in consumer:
        print (msg)

