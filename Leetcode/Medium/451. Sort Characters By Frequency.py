def frequencySort(self, s):
        
        count = Counter(s)
        max_freq = max(count.values())

        bucket = [[] for _ in range(max_freq + 1)]
        for k, v in count.items():
            bucket[v].append(k)

        stringBuilder = []
        for i in range(len(bucket)-1,0,-1):
            for c in bucket[i]:
                stringBuilder.append(c*i)

        return "".join(stringBuilder)