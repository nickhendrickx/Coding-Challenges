def findErrorNums(self, nums):
        
        num = set()
        ret = []
        for n in nums:
            if n in num:
                ret.append(n)
            num.add(n)

        for i in range(1,len(nums)+1):
            if i not in num:
                ret.append(i)
                break

        return ret 