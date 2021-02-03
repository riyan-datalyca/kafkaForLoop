# import arrayClass2
from kafka import KafkaConsumer, TopicPartition
import json
import time

topic = 'TestForLoop'
off = 0
kc = KafkaConsumer(
    'TestForLoop',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)

kc2 = KafkaConsumer(
    group_id='my-group2',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)

timeout = time.time() + 1
print(timeout)
for msg in kc:
    off = msg.offset
    print(off, timeout - time.time())
    if time.time() > timeout:
        break

print(off)

tp = TopicPartition(topic=topic, partition=0)
kc2.assign([tp])
print(tp, kc2.seek_to_end(tp))

dict = {'top': "topic",
        'msg': "EndRec",
        'tim': 1,
        'seq': 1
        }

if dict.get('seq') == 1:
    print("got seq as 1")
    dict.update({'seq': 2})
    print(dict)
