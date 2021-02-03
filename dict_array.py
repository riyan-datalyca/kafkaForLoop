dict = {}

class Data:
    def __init__(self, seq, status):
        self.seq = seq
        self.status = status

    # def addToList(self, n):
    #     Data.myList.append(n)
    #
    # def isActiveRecording(self):
    #     return any(x for x in Data.myList if x.__seq == max(x.__seq) and x.__status == "EndRec")
    #
    # def printall(self):
    #     for data in Data.myList:
    #         print(data)
