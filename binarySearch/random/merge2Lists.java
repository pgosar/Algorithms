import java.util.*;

class Solution {
    public int[] solve(int[] a, int[] b) {
        int index = 0;
        int index1 = 0;
        int anotherIndex = 0;
        int[] ans = new int[a.length + b.length];
        while (index < a.length && index1 < b.length) {
            if (a[index] > b[index1]) {
                ans[anotherIndex] = b[index1];
                index1++;
            } else {
                ans[anotherIndex] = a[index];
                index++;
            }
            anotherIndex++;
        }
        if (index < a.length) {
            while (index < a.length) {
                ans[anotherIndex] = a[index];
                index++; anotherIndex++;
            }
        }
        else if (index1 < b.length) {
            while (index1 < b.length) {
                ans[anotherIndex] = b[index1];
                index1++; anotherIndex++;

            }
        }
        return ans;
    }
}        
