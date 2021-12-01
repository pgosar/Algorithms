import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public int solve(Tree root, int lo, int hi) {
        if(root == null)
            return 0;
 
        else if(root.val < lo)
            return this.solve(root.right, lo, hi);
        
        if(root.val >= lo && root.val <= hi)
            return 1 + this.solve(root.left, lo, hi)+
                this.solve(root.right, lo, hi);
        
        else
            return this.solve(root.left, lo, hi);    
    }
}
