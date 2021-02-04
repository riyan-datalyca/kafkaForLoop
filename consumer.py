import json

from kafka import KafkaConsumer

topic = 'TestForLoop'

kc = KafkaConsumer(
    topic,
    group_id='my-group1',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)

for msg in kc:
    print(msg.value)




