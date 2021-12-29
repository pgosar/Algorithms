import java.util.*;

class Solution {
    public static int solve(int n) {
        int count = 0;
        while (n != 0) {
            System.out.println("Before: " + String.format("%16s", Integer.toBinaryString(n).replace(' ', '0')));
            n = (n & (n << 1));
            System.out.println("After: " + String.format("%16s", Integer.toBinaryString(n).replace(' ', '0')));
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(solve(156));
    }
}
