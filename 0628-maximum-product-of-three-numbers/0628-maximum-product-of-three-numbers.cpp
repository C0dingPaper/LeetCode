#include <algorithm>
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int n = nums.size();
        int a = nums[nums.size()-1];
        int b = nums[nums.size()-2];
        int c = nums[nums.size()-3];
        int three_largest = a*b*c;
        int two_largest = nums[0]*nums[1]*nums[n-1];
        return std::max(three_largest, two_largest);
    }
};