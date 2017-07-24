#This challenge is to find matching circular buffers, where matching buffers included rotated arrays
#note: a circular buffer is an array where the end points back to the beginning

from collections import Counter
class CircularBuffer(object):


    def __init__(self, list):
        self.list = list

    def __str__(self):
        return str(self.list)

    def __eq__(self, other):
        if(not isinstance(other, CircularBuffer)):
            print("not an instance of circular buffer!\n")
            return False
        if len(self.list)!=len(other.list):
            print ("lists not the same length!\n")
            return False
        return self.checkListEqual(other)

    def checkListEqual(self, other):
        #given lists are both the same length
        #checks if the list parameters are rotations of eachother
        curList = self.list
        otherList = other.list

        #wtf the least frequent elem in list
        curCnt = Counter()
        otherCnt = Counter()
        for elem in curList:
            curCnt[elem]+=1
        for elem in otherList:
            otherCnt[elem]+=1
        curLeastCommonTup = curCnt.most_common()[-1]
        otherLeastCommonTup = otherCnt.most_common()[-1]
        if curLeastCommonTup!=otherLeastCommonTup:
            return False
        leastCommonElem = curLeastCommonTup[0]
        leastCommonFreq = curLeastCommonTup[1]

        #find start for both lists
        curStart = curList.index(leastCommonElem)
        otherStart = otherList.index(leastCommonElem)

        #iterates thru other list to find beginning
        index = 0
        otherStartCount = 0
        while(index < len(otherList)):
            if self.getValue(curStart+index) != other.getValue(otherStart+index):
                index = 0
                otherStartCount += 1
                if otherStartCount>=leastCommonFreq:
                    return False
                otherStart = findNxtStart(other, leastCommonElem, otherStart) 
            index += 1
        return True


        def findNxtStart(self, other, elem, otherStart):
            for n in range(len(other.list)):
                if other.getValue(otherStart+n+1)==elem:
                    return (otherStart+n+1)%len(other.list)


        
        """start = curList[0]
        curLen = len(curList)
        otherStarts = [] #stores all indexes in otherList whose value are equal to start
        #finds indexes in otherList that are equal to curList[0] and adds them to starts
        for n in range(curLen):
            if otherList[n]==start:
                otherStarts.append(n)
        print otherStarts
        index = 0
        while index < curLen:
            step = 1
            m= 0
            while(m<len(otherStarts)):
                otherIndex = otherStarts[m]+index
                #removes index from otherStarts if value from otherStarts is not equal to the current value 
                print str(otherIndex)+":"+str(other.getValue(otherIndex)) + " " + str(index)+":"+ str(curList[index])
                if other.getValue(otherIndex)!=curList[index]:
                    otherStarts.pop(m)
                    m-=1
                m+=1
            #if self.getValue(index)==start:
                #step = index + 1
            index += step
        print len(otherStarts), otherStarts
        return len(otherStarts)!=0
        """

    
    def getValue(self, index):
        return self.list[index%len(self.list)]


####

if __name__ == '__main__':

    cb1 = CircularBuffer([1,2,3])
    cb2 = CircularBuffer([2,3,1])
    cb3 = CircularBuffer([1,2,3,4])
    cb4 = CircularBuffer([1,2,1,2,1,2,1,1])
    cb5 = CircularBuffer([1,2,1,2,1,2,1,2])
    #making sure circular buffer works
    assert(cb1.getValue(5)==cb1.getValue(2))
    
    print ("testing non-instance...")
    assert(not cb1 == 1)

    print ("testing non-length...")
    assert(not cb1 == cb3)

    print ("testing equality...")
    print ("\n cb1 vs cb2")
    assert(cb1 == cb2)
    print ("\n cb4 vs cb4")
    assert(cb4 == cb4)
    print ("\n cb5 vs cb5")
    assert(cb5 == cb5)
    print ("\n cb4 vs cb5")
    assert(not cb4 == cb5)
    #making sure eq works
    #assert(cb1==cb2)

    print ("this code kinda works!")





