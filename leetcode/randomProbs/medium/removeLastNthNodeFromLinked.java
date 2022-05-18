/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode h1 = head;
        ListNode h2 = head;
        while (n > 0) {
            h2 = h2.next;
            n--;
        }
        while (n-- > 0) h2 = h2.next;
        if (h2 == null) return head.next;
        while (h2.next != null) {
            h1 = h1.next;
            h2 = h2.next;
        }
        h1.next = h1.next.next;
        return head;
}
}

