import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    ArrayList<Integer> list = new ArrayList<>();

    public int[] solve(Tree root) {
        helper(root, 0);
        int[] arr = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            arr[i] = list.get(i);
        }
        return arr;
    }

    private void helper(Tree root, int level) {
        if (root != null) {
            if (list.size() == level) list.add(root.val);
            helper(root.left, level + 1);
            helper(root.right, level + 1);
        }
    }
}
