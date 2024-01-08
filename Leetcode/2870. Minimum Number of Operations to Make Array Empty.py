class Solution(object):
    def minOperations(self, nums):
        counter = Counter(nums)
        ans = 0

        print(counter)
        for c in counter.values():
            if c == 1: 
                return -1
            ans += (c+2)/3
            
        return ans