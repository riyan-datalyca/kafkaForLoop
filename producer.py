import json

from kafka import KafkaProducer

import listUpdates as m

kp = KafkaProducer(bootstrap_servers=['localhost:9092'],
                   value_serializer=lambda m: json.dumps(m)
                   .encode('ascii'),
                   )

while True:
    try:
        seq = m.getMaxSeq('IniRec')
        x = input("1: start Rec \t 2: Stop Rec \t 0 : stop")

        if x == '1':
            r = m.isActiveRecording(seq)
            if r:
                print(f"currently in recording . Pls Stop recording ")
            else:
                sent = kp.send('TestForLoop',
                               {'top': "topic",
                                'msg': "BegRec",
                                'tim': 1,
                                'seq': seq
                                },
                               partition=0
                               ).get(timeout=1)
        elif x == '2':
            sent = kp.send('TestForLoop',
                           {'top': "topic",
                            'msg': "EndRec",
                            'tim': 1,
                            'seq': seq
                            }
                           ).get(timeout=1)
            kp.send('TestForLoop',
                    {'top': "topic",
                     'msg': "IniRec",
                     'tim': 1,
                     'seq': seq + 1
                     }
                    ).get(timeout=1)

        elif x == '0':
            break
    except Exception as e:
        print(e)
