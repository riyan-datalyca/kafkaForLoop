import time


class Col:
    dicts = {}
    seq = 0
    def __init__(self):
        pass

    def add_data(self, json):
        # Col.dicts.update({'InitRec':0})
        pass
        # Col.dicts.
        # Col.lists.append(data)
        # if Col.dicts is None:
        #     # noinspection PyUnresolvedReferences
        #     Col.dicts.add({'InitRec': 0})
        # else:
        #     print(time.perf_counter_ns(), "added to dict", json)
        #     Col.dicts.add(json)

    def is_active_rec(self, msg, seq):
        print(Col.dicts)
        last_seq = 0
        for msg, seq in Col.dicts.items():
            print(msg, seq)

            if msg == 'BegInf' and seq >= last_seq:
                # print("h")
                last_seq = seq
        for msg, seq in Col.dicts.items():
            if msg == 'EndInf' and seq == last_seq:
                return False
            else:
                return True

    def is_active_inf(self):
        last_seq = 0
        for msg, seq in Col.dicts.items():
            if msg == 'BegInf' and seq >= last_seq:
                last_seq = seq

        for msg, seq in Col.dicts.items():
            if msg == 'EndRInf' and seq == last_seq:
                Col.seq = last_seq + 1
                return False
            else:
                return True

    def get_new_seq(self):
        return Col.seq

    # def
    def testig(self):
        last_seq = 0
        if Col.dicts is None:
            print(time.perf_counter_ns(), "no values in dicts")
            return None
        else:
            for msg, seq in Col.dicts.items():
                if msg == 'BegRec':
                    last_seq = seq

        for msg, seq in Col.dicts.items():
            if msg == 'EndRec' and seq == last_seq:
                print(f'{time.perf_counter_ns()}Recording stopped of seq: {seq}')
            elif msg == 'EndRec' and seq != last_seq:
                print(f'{time.perf_counter_ns()}still recording of seq: {last_seq}')

        # if Col.lists is None:
        #     print("No Values In List")
        # for i in Col.lists:
        #     print(i)
