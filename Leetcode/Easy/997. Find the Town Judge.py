def findJudge(self, n, trust):
        if not trust:
            if n == 1:
                return 1
            return -1

        xmap = {}
        ymap = {}
        for x,y in trust:
            xmap[x] = xmap.get(x,0) + 1
            ymap[y] = ymap.get(y,0) + 1

        print(xmap)
        print(ymap)
        for y, v in ymap.items():
            if v == n - 1 and y not in xmap.keys():
                return y

        return -1