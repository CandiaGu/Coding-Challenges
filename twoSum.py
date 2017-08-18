'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    #sort nums
    setNums = set(num)

    for num in setNums:
        if (target - num) in setNums:
            num1 = num
            num2 = target-num
            break
    index1 = nums.index(num1)
    if num1!=num2:
        index2 = nums.index(num2)
    else:
        index2 = nums.index(num2, index1+1)
    return index1, index2


if __name__ == '__main__':
    

