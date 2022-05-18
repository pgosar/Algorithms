import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public boolean solve(Tree root, int val) {
        while(root != null && root.val != val){
            root = val < root.val ? root.left : root.right;
        }
        if (root != null) {
            return true;
        }
        return false;
    }
}
