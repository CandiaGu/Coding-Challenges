# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val)

def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = True
        overFl = 0
        prevNode = None
        while l1 != None or l2 != None or overFl != 0:
            num1 = l1.val if l1!=None else 0
            num2 = l2.val if l2!=None else 0
            tot = num1+num2+overFl
            curNode = ListNode(tot%10)
            overFl = tot/10
            #print overFl
            if first:
                firstNode = curNode
                first = False
            if prevNode!=None:
                prevNode.next = curNode
            prevNode = curNode

            if l1!= None:l1 = l1.next
            if l2!=None:l2 = l2.next
        return firstNode

if __name__ == '__main__':
    l1 = ListNode(1);# l1.next = ListNode(1)#; l1.next.next = ListNode(3)
    l2 = ListNode(9); l2.next = ListNode(9);# l2.next.next = ListNode(4)
    l3 = addTwoNumbers(l1, l2)
    print l3, l3.next, l3.next.next