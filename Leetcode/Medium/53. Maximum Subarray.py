def maxSubArray(self, nums: List[int]) -> int:

        l, r = 0,1
        max = nums[l]
        sum = nums[l]

        while r < len(nums):
            if nums[r] + sum < nums[r]:
                sum = nums[r]
            else:
                sum = sum + nums[r]

            if sum > max:
                max = sum
                    
            r = r+1

        return max