def findMaxLength(self, nums: List[int]) -> int:
        hmap = {}
        count = 0
        maxlen = 0
        hmap[0] = -1

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            print(count)
            if count in hmap:
                maxlen = max(maxlen, i - hmap[count])
            
            else:
                hmap[count] = i

        return maxlen