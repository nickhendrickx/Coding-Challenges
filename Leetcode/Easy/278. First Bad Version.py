def firstBadVersion(self, n: int) -> int:
        l, r = 1, n


        # [1,1,1,1,0,0,0,0,0]
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid-1
            else:
                l = mid+1

        return l