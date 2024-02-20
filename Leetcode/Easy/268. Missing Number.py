def missingNumber(self, nums):
        
        total_sum = sum(nums)
        total = len(nums) * (len(nums)+1) /2
        return total-total_sum