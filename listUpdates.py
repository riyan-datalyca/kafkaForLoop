import json
import threading

from kafka import KafkaConsumer

from dataObject import Data

myList = []
topic = 'TestForLoop'
seqValue = 0


def RefreshList():
    global myList
    kc = KafkaConsumer(
        topic,
        group_id='my-group1',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=False,
        consumer_timeout_ms=6000,
        value_deserializer=lambda m: json.loads(m.decode('ascii'))
    )
    for msg in kc:
        myList.append(Data(msg.value['seq'], msg.value['msg']))


def getMaxSeq(query):
    RefreshList()
    global myList
    if myList:
        maxSeq = 1
        for data in myList:
            if data.status == query:
                maxSeq = maxSeq < int(data.seq) and int(data.seq) or maxSeq
        return maxSeq
    else:
        return 1


def incrementMaxSeq(query):
    global seqValue
    maxSeq = 0
    for data in myList:
        if data.status == query:
            maxSeq = maxSeq < int(data.seq) and int(data.seq) or maxSeq
    seqValue = maxSeq + 1


def isActiveRecording(query):
    maxSeq = 0
    for data in myList:
        if data.status == 'BegRec' and data.seq == query:
            maxSeq = maxSeq < int(data.seq) and int(data.seq) or maxSeq
            if data.status == 'EndRec' and data.seq == maxSeq:
                return False
            else:
                return True


def isActiveInference(query):
    maxSeq = 0
    for data in myList:
        if data.status == 'BegInf' and data.seq == query:
            maxSeq = maxSeq < int(data.seq) and int(data.seq) or maxSeq
            if data.status == 'EndInf' and data.seq == maxSeq:
                return False
            else:
                return True


if __name__ == '__main__':
    t1 = threading.Thread(target=RefreshList())
    t1.start()
