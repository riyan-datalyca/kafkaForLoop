from kafka import KafkaConsumer
import json
import time
from arrayClass import Col
import arrayClass2

c = Col()
kc = KafkaConsumer(
    'TestForLoop',
    group_id='my-group2',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)


for msg in kc:
    # time.sleep(1)
    print(msg.value)
    # c.add_data({msg.value['msg']: msg.value['seq']})
    if arrayClass2.is_active_rec():
        print(time.perf_counter_ns(),"recording is in progress")

    if arrayClass2.is_active_inf():
        print(time.perf_counter_ns(),"inference is active")

    if msg.value['msg'] == 'EndInf':
        arrayClass2.seq += 1
