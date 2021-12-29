class Solution {
    public LLNode solve(LLNode node) {
        if (node == null || node.next == null) {
            return node;
        }
        LLNode temp = node.next;
        node.next = solve(node.next.next);
        temp.next = node;
        return temp;
    }
}
