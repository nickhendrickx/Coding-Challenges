def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid

            #[6,7,1,2,3,4,5]
            if nums[mid] < nums[r]:
                if nums[mid] > target:
                    r=mid-1
                else:
                    if nums[mid] < target and target <= nums[r]:
                        l =mid+1
                    else:
                        r = mid-1

            #[3,4,5,6,7,1,2]
            else:
                if nums[mid] < target:
                    l = mid+1
                else:
                    if nums[mid] > target and target >= nums[l]:
                        r = mid-1
                    else:
                        l = mid+1

        return -1