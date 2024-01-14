def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False

        oneMap = defaultdict(int)
        twoMap = defaultdict(int)

        for c in word1:
            oneMap[c] += 1

        for c in word2:
            twoMap[c] += 1

        if sorted(oneMap.keys()) != sorted(twoMap.keys()):
            return False

        threeMap = defaultdict(int)
        fourMap = defaultdict(int)

        for v in oneMap.values():
            threeMap[v] += 1

        for v in twoMap.values():
            fourMap[v] += 1
            
        return threeMap == fourMap