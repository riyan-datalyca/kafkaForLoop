from kafka import KafkaConsumer, TopicPartition
import json

topic = 'TestForLoop'
kc = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)

seq = 1

tp = TopicPartition(topic, 0)
kc.assign([tp])


def get_seq():
    if kc.seek_to_end(tp) is None:
        return seq
    else:
        return seq


def is_active_rec():
    last_seq = 0
    off = kc.seek_to_end(tp) if kc.seek_to_end(tp) != None else 0
    print("rec offset", off)
    for msg in kc:
        if msg.value['msg'] == 'BegRec' and msg.value['seq'] > last_seq:
            print("Recording")
            last_seq = msg.value['seq']
        elif msg.value['msg'] == 'EndRec' and msg.value['seq'] > last_seq:
            print("Recording stopped")
            last_seq = msg.value['seq']
        elif msg.offset == off - 1:
            print("read all messages")
            break
        else:
            # print("for loop giving error")
            break


def is_active_inf():
    last_seq = 0
    off = kc.seek_to_end(tp) if kc.seek_to_end(tp) != None else 0
    # print(off)
    for msg in kc:
        if msg.value['msg'] == 'BegInf' and msg.value['seq'] > last_seq:
            print("Inferencing")
            last_seq = msg.value['seq']
        elif msg.offset == off - 1:
            print("read all messages")
            break
        else:
            # print("for loop giving error")
            break
