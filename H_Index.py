""" H-index : A scientist has index h is h of his/her N papers have at least h citations each, and the other N - H papers
have not more than h citations each."""
#if multiple h-indexes, max is returned

def findHIndex(cit):
    #sort num of citations O(nlogn)
    #import pdb; pdb.set_trace()

    cit.sort()
    print(cit)
    n = len(cit)

    #find the h-index using binary search since h-index can be btwn 0 and n inclusive
    return findIndexHelper(cit, 1, n-1, n/2)

def findIndexHelper(cit, lo, hi, potH):
    '''
    cit - citations list
    lo - lower index
    hi - higher index
    potH - potential h-index
    '''
    # base case
    #if lo == hi:
    #    return lo

    higherIndex = potH + (hi-potH)/2
    lesserIndex = lo + (potH - lo)/2
    if potH < len(cit) and potH > 0: # not edge cases
        # check h-index conditions
        if isValidHIndex(cit, potH):
            # find max h-index
            if not isValidHIndex(cit, potH+1):
                return True
            else:
                return findIndexHelper(cit, potH + 1, hi, higherIndex)
        else:
            if cit[-potH-1] > potH:# too big
                return findIndexHelper(cit, lo, potH-1, lesserIndex)
            else:
                return findIndexHelper(cit, potH + 1, hi, higherIndex)
    else:
        if isValidHIndex(potH):
            return potH

def isValidHIndex(cit, potH):

    #import pdb; pdb.set_trace()
    numCit = cit[-potH]
    
    if potH > 0 and potH < len(cit): # not edge cases
        prevNumCit = cit[-potH-1]
        return numCit >= potH and prevNumCit <= potH
    else: #edge cases
        if potH == 0 and len(cit) == 0:
            return True
        if potH == len(cit):
            return cit[potH-1] <= potH
    return False


####

if __name__ == '__main__':
    cit = [3,0,6,1,5]
    #print findHIndex(cit)
    cit.sort()
    #print isValidHIndex(cit, 3)
    for i in range(6):
        print(i);print(":")
        print(isValidHIndex(cit, i))
    print findHIndex(cit)
    assert(findHIndex(cit) == 3)

