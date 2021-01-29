class Col:
    dicts = {}
    def __init__(self):
        pass

    def add_data(self, data, json):
        # Col.lists.append(data)
        print(json)
        Col.dicts.update(json)

    def get_data(self):
        last_seq = 0
        if Col.dicts is None:
            print("no values in dicts")
            return None
        else:
            for msg, seq in Col.dicts.items():
                if msg == 'BegRec':
                    last_seq = seq

        for msg, seq in Col.dicts.items():
            if msg == 'EndRec' and seq == last_seq:
                print(f'Recording stopped of seq: {seq}')
            elif msg =='EndRec' and seq != last_seq:
                print(f'still recording of seq: {last_seq}')

        # if Col.lists is None:
        #     print("No Values In List")
        # for i in Col.lists:
        #     print(i)
