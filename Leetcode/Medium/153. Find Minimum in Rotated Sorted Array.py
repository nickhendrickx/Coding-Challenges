def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r)//2
            nr = nums[mid]

            if nr < nums[r]:
                r = mid

            elif nr > nums[r]:
                l = mid+1

        return nums[l]