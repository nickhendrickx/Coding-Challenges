def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        onelist = {}

        for i in nums1:
            onelist[i] = 1

        ret = set()
        for i in nums2:
            if onelist.get(i) == 1:
                ret.add(i)

        return ret