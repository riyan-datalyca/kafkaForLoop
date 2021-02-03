from dict_array import Data
from kafka import KafkaConsumer, TopicPartition
import json

myList = []
topic = 'TestForLoop'
seqValue = 0

def RefreshList():
    kc = KafkaConsumer(
        group_id='my-group1',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        value_deserializer=lambda m: json.loads(m.decode('ascii'))
    )
    tp = TopicPartition(topic, 0)
    print(tp)
    kc.assign([tp])
    off = kc.seek_to_beginning()
    myList = []
    print('last offset',off)
    for msg in kc:
        print(msg.offset)
        myList.append(Data(msg.value['seq'], msg.value['msg']))
        if off == msg.offset:
            print("helllo")
    print('after for loop')

def getSeq():
    RefreshList()
    return seqValue

def getMaxSeq(query):
    RefreshList()
    maxSeq = 0
    for data in myList:
        if data.status == query:
            maxSeq = maxSeq < int(data.seq) and int(data.seq) or maxSeq
    return maxSeq

def incrementMaxSeq(query):
    RefreshList()
    global seqValue
    maxSeq = 0
    for data in myList:
        if data.status == query:
            maxSeq = maxSeq < int(data.seq) and int(data.seq) or maxSeq
    seqValue = maxSeq +1
    # if seq > getMaxSeq('EndRec'):



def isActiveRecording():
    return getMaxSeq('BegRec') > getMaxSeq('EndRec') and True or False


def isActiveInference():
    return getMaxSeq('BegInf') > getMaxSeq('EndInf') and True or False


if __name__ == '__main__':
    RefreshList()