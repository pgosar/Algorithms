#include <cstdio>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            if (map.count(target-nums[i])>0) {
                return {map[target - nums[i]], i};
            }
            map[nums[i]]=i;
        }
            return {};

    }
};