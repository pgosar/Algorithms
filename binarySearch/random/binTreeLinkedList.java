import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */

/**
 * class LLNode {
 *   int val;
 *   LLNode next;
 * }
 */
class Solution {
    public LLNode solve(Tree root) {
        LLNode head = new LLNode();
        LLNode curr = head;
        helper(root, head, curr);
        return head.next;
    }
    public void helper(Tree root, LLNode head, LLNode curr) {
        if (root != null) {
            helper(root.left, head, curr);
            curr.next = new LLNode(root.val);
            curr = curr.next;
            helper(root.right, head, curr);
        }
    }
}
