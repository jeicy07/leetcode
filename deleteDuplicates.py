# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head
        else:
            cur = pos = head
            while cur.next is not None:
                pos = cur.next
                while pos is not None and cur.val == pos.val:
                    pos = pos.next
                if pos is not None:
                    cur.next = pos
                    cur = cur.next
                else:
                    cur.next = None
                    return head
            return head
                    
                    
                    
                
                
        """
        :type head: ListNode
        :rtype: ListNode
        """