import java.util.*;

class Solution {
    public boolean solve(int n, int[][] friends) {
        HashSet<Integer> friend = new HashSet<>();
        for (int i = 0; i < friends.length; i++) {
            friend.add(friends[i][0]);
            friend.add(friends[i][1]);
        }
        return friend.size() == n;
    }
}
