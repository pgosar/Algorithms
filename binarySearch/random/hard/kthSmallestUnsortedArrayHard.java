import java.util.*;

class Solution {
    public int solve(int[] nums, int k) {
        return quick(nums, k, 0, nums.length - 1);
    }

    public static int quick(int[] arr, int k, int left, int right) {
        int pivot = arr[right];
        int pi = helper(arr, pivot, left, right);
        if (k < pi) return quick(arr, k, left, pi - 1);
        else if (k > pi) return quick(arr, k, pi + 1, right);
        else return arr[pi];
    }

    public static int helper(int[] arr, int pivot, int left, int right) {
        int i = left, j = left;
        while (i <= right) {

            if (arr[i] > pivot) i++;
            else {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++; j++;
            }
        }
        return j - 1;
    }
}
