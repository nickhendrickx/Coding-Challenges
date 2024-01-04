def customSortString(self, order, s):
        
        hmap = {}
        for c in s:
            hmap[c] = 1 + hmap.get(c,0)

        print(hmap)

        ret = ""
        for c in order:
            if c in hmap:
                ret += c * hmap[c] 
                hmap[c] = 0

        for k, v in hmap.items():
            if v != 0:
                ret += k * v
                
        return ret