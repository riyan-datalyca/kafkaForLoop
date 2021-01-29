from kafka import KafkaConsumer
import json
import time
from arrayClass import Col

c = Col()
kc = KafkaConsumer(
    'TestForLoop',
    group_id='my-group2',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)

for msg in kc:
    # time.sleep(1)
    print(msg.value)
    c.add_data(msg.value['tim'], {msg.value['msg']:
                                  msg.value['seq'],
                                  })
    c.get_data()

