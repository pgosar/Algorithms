class Solution {
    public int solve(LLNode node, int k) {
        if (node == null) {
            return 0;
        }
        int num = k;
        LLNode temp = node;
        while (num >= 0) {
            temp = temp.next;
            num--;
        }
        LLNode head = node;
        while (temp != null) {
            temp = temp.next;
            head = head.next;
        }
        return head.val;
    }
}
