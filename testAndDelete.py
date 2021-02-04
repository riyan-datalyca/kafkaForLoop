from threading import Thread
import time
from dict_array import Data
from kafka import KafkaConsumer, TopicPartition
import json, threading

list = []# global variable
topic = 'TestForLoop'
seqValue = 0

def thread1(threadname):
    global list
    list = []
    kc = KafkaConsumer(
        topic,
        group_id='my-group1',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda m: json.loads(m.decode('ascii'))
    )
    for msg in kc:
        # print(msg.offset)
        list.append(Data(msg.value['seq'], msg.value['msg']))
        # updateList(myList2)

def thread2(threadname):
    global list
    if list:
        for i in list:
            print(i.seq, i.status)
    else:
        print("error")
    # for k in range(100):
    #     print(len(list))
    #     time.sleep(1)


thread1 = Thread(target=thread1, args=("Thread-1",))
# thread2 = Thread(target=thread2, args=("Thread-2",))

thread1.start()

while True:
    x = input('enter 1 to get data')
    if x == '1':
        thread2('a')
    else:
        break
# thread2.start()

thread1.join()
# thread2.join()