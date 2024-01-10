class Solution {
public:
    int singleNumber(vector<int>& nums) {
        std::map<int,int> m;
        for(int i = 0; i < nums.size(); i++) {
            m[nums[i]]++;
        }
        
        int sol;
        for (const auto& [key, value] : m) {
            if (value == 1)
                sol = key;
        }
        return sol;
    }
};