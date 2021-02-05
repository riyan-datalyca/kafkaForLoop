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

for data in kc:
    msg = data.value['msg']
    seq = data.value['seq']
    print(data.value)
    # if msg == 'IniRec':
    #     P.send('BegRec')





