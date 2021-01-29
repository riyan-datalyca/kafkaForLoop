dicts = {}


def add_data(data, json):
    dicts.update(json)
    print(json)


def get_data():
    print(dicts.items())
    for msg, seq in dicts.items():
        if  msg == 'initRec':
            print(f'got {msg}, prerparing to start video')
        if msg == 'endRec' and seq !=0:
            print(f'Recording of seq: {seq-1} not cmpleted')


def runfunc():
    add_data(1, {'initRec': 1})
    add_data(1, {'endRec': 1})
    get_data()


if __name__ == '__main__':
    runfunc()
