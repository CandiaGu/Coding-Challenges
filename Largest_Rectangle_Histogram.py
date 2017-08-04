'''
Given n non-negative integers representing the histogram's bar height where the width of 
each bar is 1, find the area of largest rectangle in the histogram.
'''
def findLargestHistRectangle(heights):
    heights = list(reversed(heights))
    curRects = {} # height: width
    maxRect = 0
    heights.append(0)
    for idx, bar in enumerate(heights):
        if not any(curRects) and bar!= 0: # if dict is empty
            curRects[bar] = 1
            area = bar
            if area > maxRect: 
                maxRect = area
        else:
            sortedKeys = sorted(curRects, key = curRects.get, reverse = True)# sorted by width
            lastWidth = 0
            for k in sortedKeys:
                if bar >= k:
                    curRects[k] += 1
                elif bar < k: #end of a rect
                    area = k * curRects[k]
                    if area > maxRect: 
                        maxRect = area
                    if lastWidth==0:
                        lastWidth = curRects.pop(k)
                        print "lw", lastWidth
                    else :
                        curRects.pop(k)
            if idx > 0 and bar > heights[idx-1]:
                curRects[bar] = 1            
            if idx > 0 and bar != 0 and bar < heights[idx-1] and bar not in sortedKeys: #and bar not in curRects.keys():
                curRects[bar] = lastWidth+1
        print bar, curRects, maxRect

    return maxRect


###
if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    assert(findLargestHistRectangle(heights) == 10)
    print 

    heights = [2,0,2]
    assert(findLargestHistRectangle(heights) == 2)
    print

    heights = [2,1,2]
    assert(findLargestHistRectangle(heights) == 3)
    print

    heights = [3,6,5,7,4,8,1,0]
    assert(findLargestHistRectangle(heights) == 20)
    print

    heights = [2,1,2,0,3,2,2,3]
    assert(findLargestHistRectangle(heights) == 8)
    print 

    

    print "Passed!"