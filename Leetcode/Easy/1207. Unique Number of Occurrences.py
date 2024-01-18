def uniqueOccurrences(self, arr):
        
        occ = defaultdict(int)
        for i in arr:
            occ[i] += 1

        num = set()
        for _, v in occ.items():
            if v in num:
                return False
            num.add(v)

        return True