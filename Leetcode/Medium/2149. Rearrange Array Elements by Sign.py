def rearrangeArray(self, nums):
        p, m = 0, 0
        ret = []
        while len(ret) != len(nums):
            while nums[p] < 0:
                p += 1
            ret.append(nums[p])
            p += 1
            
            while nums[m] > 0:
                m += 1
            ret.append(nums[m])
            m += 1
            

        return ret