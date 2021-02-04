from dict_array import Data
from kafka import KafkaConsumer, TopicPartition
import json, threading, time

# global myList
myList = []
topic = 'TestForLoop'
seqValue = 0


def RefreshList():
    global myList
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
        # print(msg.offset)
        myList.append(Data(msg.value['seq'], msg.value['msg']))
        # updateList(myList)
        # getMaxSeq('a')
        # print(myList)
        # return myList


def updateList(list):
    global myList
    myList = list
    print(myList[0], list[0])


def getSeq():
    # global seqValue
    return seqValue


def getMaxSeq(query):
    global myList
    if myList:
        for i in myList:
            print(i.seq, i.status)
    else:
        print("error")
        return False
    maxSeq = 0
    for data in myList:
        print(data.seq)
        if data.status == query:
            # print(data.seq)
            maxSeq = maxSeq < int(data.seq) and int(data.seq) or maxSeq
    return maxSeq


def incrementMaxSeq(query):
    # global myList
    global seqValue
    maxSeq = 0
    for data in myList:
        if data.status == query:
            maxSeq = maxSeq < int(data.seq) and int(data.seq) or maxSeq
    seqValue = maxSeq + 1
    # if seq > getMaxSeq('EndRec'):


def isActiveRecording():
    return getMaxSeq('BegRec') > getMaxSeq('EndRec') and True or False


def isActiveInference():
    return getMaxSeq('BegInf') > getMaxSeq('EndInf') and True or False


if __name__ == '__main__':
    print("main called")

    t1 = threading.Thread(target=RefreshList())
    t1.start()
    # getMaxSeq('a')
    # print(t1.join())
