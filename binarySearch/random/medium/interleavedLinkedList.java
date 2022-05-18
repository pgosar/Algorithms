import java.util.*;

/**
 * class LLNode {
 *   int val;
 *   LLNode next;
 * }
 */
class Solution {
    public LLNode solve(LLNode l0, LLNode l1) {
        LLNode ans = new LLNode();
        LLNode temp = ans;
        while (l0 != null && l1 != null) {
            ans.next = l0;
            ans = ans.next;
            l0 = l0.next;
            ans.next = l1;
            ans = ans.next;
            l1 = l1.next;
        }

        if (l0 != null) ans.next = l0;
        if (l1 != null) ans.next = l1;
        return temp.next;
    }
}
