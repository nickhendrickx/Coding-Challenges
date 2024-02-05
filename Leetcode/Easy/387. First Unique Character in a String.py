def firstUniqChar(self, s):
        
        hmap = {}
        for c in s:
            hmap[c] = hmap.get(c,0) + 1

        for i, c in enumerate(s):
            if hmap[c] == 1:
                return i
        
        return -1