from kafka import KafkaProducer
import json
import time

kp = KafkaProducer(bootstrap_servers=['localhost:9092'],
                   value_serializer=lambda m: json.dumps(m)
                   .encode('ascii'),
                   )


sent = kp.send('TestForLoop',
            {'top': "topic",
             'msg': "IniRec",
             'tim': 1,
             'seq': 0
             }
            ).get(timeout=1)
print(sent.offset, sent.partition)

time.sleep(1)

sent = kp.send('TestForLoop',
            {'top': "topic",
             'msg': "BegRec",
             'tim': 1,
             'seq': 0
             }
            ).get(timeout=1)
print(sent.offset, sent.partition)

time.sleep(1)

sent = kp.send('TestForLoop',
            {'top': "topic",
             'msg': "EndRec",
             'tim': 1,
             'seq': 0
             }
            ).get(timeout=1)
print(sent.offset, sent.partition)

time.sleep(1)

sent = kp.send('TestForLoop',
            {'top': "topic",
             'msg': "IniInf",
             'tim': 1,
             'seq': 0
             }
            ).get(timeout=1)
print(sent.offset, sent.partition)

time.sleep(1)
# for i in range(0, 100):
#     time.sleep(1)
#     sent = kp.send('TestForLoop',
#             {'top': "topic",
#              'msg': "IniRec",
#              'tim': i,
#              'seq': 0
#              }
#             ).get(timeout=1)
#     print(sent.offset, sent.partition)
