def connectSticks(self, sticks):
        heapq.heapify(sticks)
        total = 0
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            total += first + second
            heapq.heappush(sticks,first+second)

        return total 