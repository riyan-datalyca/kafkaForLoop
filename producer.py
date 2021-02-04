from kafka import KafkaProducer
import json
import time
import maindictarray as m

kp = KafkaProducer(bootstrap_servers=['localhost:9092'],
                   value_serializer=lambda m: json.dumps(m)
                   .encode('ascii'),
                   )

while True:
    try:
        # if m.isActiveRecording():
        #     print(time.perf_counter_ns(), "recording is in progress")
        #
        # if m.isActiveInference():
        #     print(time.perf_counter_ns(), "inference is active")

        x = input("1: start Rec \t 2: Stop Rec \t 0 : stop")

        if x == '1':
            sent = kp.send('TestForLoop',
                           {'top': "topic",
                         'msg': "BegRec",
                         'tim': 1,
                         'seq': m.getSeq() + 1
                         },
                           partition=0
                        ).get(timeout=1)
            # sent1 = kp.send('TestForLoop',
            #                {'top': "topic",
            #                 'msg': "BegRec",
            #                 'tim': 1,
            #                 'seq': m.getSeq() + 1
            #                 },
            #                partition=1
            #                ).get(timeout=1)
            print(m.getSeq() + 1)
        elif x == '2':
            sent = kp.send('TestForLoop',
                           {'top': "topic",
                            'msg': "EndRec",
                            'tim': 1,
                            'seq': m.getMaxSeq('BegRec')
                            }
                           ).get(timeout=1)
            # sent1 = kp.send('TestForLoop',
            #                {'top': "topic",
            #                 'msg': "EndRec",
            #                 'tim': 1,
            #                 'seq': m.getMaxSeq('BegRec')
            #                 },
            #                 partition=1
            #                ).get(timeout=1)
            # print(m.getMaxSeq('BegRec'))
        elif x == '0':
            break
    except Exception as e:
        print(e)
