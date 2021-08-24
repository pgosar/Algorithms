# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        head = final = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                final.next = l1
                final = final.next
                l1 = l1.next
            else:
                final.next = l2
                final = final.next
                l2 = l2.next
        final.next = l1 or l2
        return head.next

    
