def majorityElement(self, nums):
        majority = len(nums)/2 
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num,0) + 1
            if hmap[num] > majority:
                return num

        return -1