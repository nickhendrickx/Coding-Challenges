def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i, num in enumerate(nums):
            compl = target - num
            if compl in sums:
                return [sums[compl], i]
            else:
                sums[num] = i