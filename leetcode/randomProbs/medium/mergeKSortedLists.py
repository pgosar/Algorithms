# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        heap = []
        ans = head = ListNode(0)
        for i in lists:
            if i:
                heapq.heappush(heap, i)
        while heap:
            node = heapq.heappop(heap)
            head.next = node
            head = head.next
            if node.next:
                heapq.heappush(heap, node.next)
        return ans.next
