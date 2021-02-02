from kafka import KafkaProducer
import json
import time
import arrayClass2 as a2

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
                         'seq': a2.get_seq()
                         }
                        ).get(timeout=1)
            print(sent.offset, sent.partition)
        elif x == '2':
            sent = kp.send('TestForLoop',
                           {'top': "topic",
                            'msg': "EndRec",
                            'tim': 1,
                            'seq': a2.get_seq()
                            }
                           ).get(timeout=1)
            print(sent.offset, sent.partition)
        else:
            break
    except Exception as e:
        print(e)

# sent = kp.send('TestForLoop',
#             {'top': "topic",
#              'msg': "IniRec",
#              'tim': 1,
#              'seq': 1
#              }
#             ).get(timeout=1)
# print(sent.offset, sent.partition)
#
# time.sleep(1)
#
# sent = kp.send('TestForLoop',
#             {'top': "topic",
#              'msg': "BegRec",
#              'tim': 1,
#              'seq': 1
#              }
#             ).get(timeout=1)
# print(sent.offset, sent.partition)
#
# time.sleep(1)
#
# sent = kp.send('TestForLoop',
#             {'top': "topic",
#              'msg': "EndRec",
#              'tim': 1,
#              'seq': 1
#              }
#             ).get(timeout=1)
# print(sent.offset, sent.partition)
#
# time.sleep(1)
#
# sent = kp.send('TestForLoop',
#             {'top': "topic",
#              'msg': "IniInf",
#              'tim': 1,
#              'seq': 1
#              }
#             ).get(timeout=1)
# print(sent.offset, sent.partition)
#
# time.sleep(1)
#
# sent = kp.send('TestForLoop',
#             {'top': "topic",
#              'msg': "BegInf",
#              'tim': 1,
#              'seq': 1
#              }
#             ).get(timeout=1)
# print(sent.offset, sent.partition)
#
# time.sleep(1)
#
# sent = kp.send('TestForLoop',
#             {'top': "topic",
#              'msg': "BegRec",
#              'tim': 1,
#              'seq': 2
#              }
#             ).get(timeout=1)
# print(sent.offset, sent.partition)
#
# time.sleep(1)
#

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
