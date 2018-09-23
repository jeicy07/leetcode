# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        add1 = l1
        add2 = l2
        
        pre = (add1.val + add2.val) % 10
        comp = (add1.val + add2.val) / 10
        result = tmp = ListNode(pre)
        add1 = add1.next
        add2 = add2.next

                
        while add1 is not None and add2 is not None:
            pre = (add1.val + add2.val + comp) % 10
            newtmp = ListNode (pre)
            tmp.next = newtmp
            tmp = tmp.next
            comp = (add1.val + add2.val + comp) / 10
            add1 = add1.next
            add2 = add2.next
            
        
        if add1 is None and add2 is None and comp != 0:
            newtmp = ListNode(comp)
            tmp.next = newtmp
        elif add1 is not None and comp == 0:
            tmp.next  = add1
        elif add1 is not None and comp != 0:
            while add1 is not None:
                pre = (add1.val + comp) % 10
                newtmp = ListNode (pre)
                tmp.next = newtmp
                tmp = tmp.next
                comp = (add1.val + comp) / 10
                add1 = add1.next
            if comp != 0:
                newtmp = ListNode (comp) 
                tmp.next = newtmp 
        elif add2 is not None and comp == 0:
            tmp.next = add2
        elif add2 is not None and comp != 0:
            while add2 is not None:
                pre = (add2.val + comp) % 10
                newtmp = ListNode (pre)
                tmp.next = newtmp
                tmp = tmp.next
                comp = (add2.val + comp) / 10
                add2 = add2.next
            if comp != 0:
                newtmp = ListNode (comp) 
                tmp.next = newtmp


        
        return result


