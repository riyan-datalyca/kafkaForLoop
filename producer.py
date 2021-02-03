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
        x = input("1: start Rec \t 2: Stop Rec \t 0 : stop")

        if x == '1':
            sent = kp.send('TestForLoop',
                           {'top': "topic",
                         'msg': "BegRec",
                         'tim': 1,
                         'seq': m.getSeq()
                         }
                        ).get(timeout=1)
            print(sent.offset, sent.partition)
        elif x == '2':
            sent = kp.send('TestForLoop',
                           {'top': "topic",
                            'msg': "EndRec",
                            'tim': 1,
                            'seq': m.getMaxSeq('BegRec')
                            }
                           ).get(timeout=1)
            print(sent.offset, sent.partition)
        else:
            break
    except Exception as e:
        print(e)

class KafkaProd:

    def __init__(self, topic, json):
        self.topic = topic
        self.json = json
        if json.get('seq') == 0:
            print("got seq as 0")
            self.json.update({'seq': 1})
            print(self.json)