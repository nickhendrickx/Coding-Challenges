def largestPerimeter(self, nums):
        if len(nums) < 3:
            return -1

        nums.sort()
        total = 0
        ret = -1

        for side in nums:
            if total > side:
                ret = total + side
            total += side
        return ret