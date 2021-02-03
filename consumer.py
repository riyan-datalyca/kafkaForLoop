from kafka import KafkaConsumer, TopicPartition
import json
import time
# import maindictarray

topic = 'TestForLoop'
kc = KafkaConsumer(
    group_id='my-group0',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)
tp = TopicPartition(topic=topic, partition=0)
kc.assign([tp])

for msg in kc:
    print(msg.value)
    # if msg.value['msg'] == 'EndRec':
    #     # maindictarray.RefreshList()
    #     maindictarray.incrementMaxSeq(msg.value['msg'])
    #     print(maindictarray.getSeq())
    #
    # if maindictarray.isActiveRecording():
    #     print(time.perf_counter_ns(),"recording is in progress")
    #
    # if maindictarray.isActiveInference():
    #     print(time.perf_counter_ns(),"inference is active")
