def minSteps(self, s, t):
        
        s_map = {}

        for c in s:
            s_map[c] = s_map.get(c,0) + 1

        for c in t:
            s_map[c] = s_map.get(c,0) - 1
        
        total = 0
        for v in  s_map.values():
            total += abs(v)

        return total / 2