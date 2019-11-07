from functools import reduce
class kane:
    def __init__(self,myList):
        self.list = myList
    def getMean(self):
        return reduce(lambda a,b:a+b, self.list)/len(self.list)
    def getMedian(self):
        copyList = self.list.copy()
        copyList.sort()
        l = len(copyList)
        mid = int(l/2)
        if l % 2 == 1:
            return copyList[mid+1]
        else:
            return(copyList[mid-1] + copyList[mid])/2
    def getMode(self):
        copySet = self.list.copy()
        copySet.sort()
        copySet = list(set(copySet))

        countSet = list(map(lambda a: self.list.count(a), copySet))
        return copySet[countSet.index(max(countSet))]