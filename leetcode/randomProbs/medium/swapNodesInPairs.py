# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur and cur.next:
            prev.next=cur.next
            cur.next = cur.next.next
            prev.next.next = cur
            prev = cur
            cur = cur.next
        return dummy.next
