from kafka import KafkaConsumer, TopicPartition, KafkaProducer
import json
import time

topic = 'TestForLoop'

kp = KafkaProducer(bootstrap_servers=['localhost:9092'],
                   value_serializer=lambda m: json.dumps(m)
                   .encode('ascii'),
                   )

kc = KafkaConsumer(
    group_id='my-group1',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)
tp = TopicPartition(topic=topic, partition=0)
kc.assign([tp])

for msg in kc:
    print(msg.value)
    if msg.value['msg'] == 'EndRec':
        kp.send('TestForLoop',
                {'top': "topic",
                 'msg': "IniRec",
                 'tim': 1,
                 'seq': msg.value['seq'] + 1
                 }
                ).get(timeout=1)



