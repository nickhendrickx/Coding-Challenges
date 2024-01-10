class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0;
        int index2 = 0;
        int output = 0;
        
        for(int index1 = 1; index1 < nums.size(); index1++) {
            if (nums[index1] == nums[index2]) {
                nums[index1] = -1;
                
            }
            else {
                nums[++index2] = nums[index1];
                
                
            }    
            
        }
        return index2+1;
    }
};