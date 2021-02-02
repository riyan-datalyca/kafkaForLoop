from kafka import KafkaConsumer
import json
import time

kc = KafkaConsumer(
    'TestForLoop',
    group_id='my-group2',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)


print(time.perf_counter_ns())
# for msg in kc:
#     time.sleep(1)
#     print(msg.value)
