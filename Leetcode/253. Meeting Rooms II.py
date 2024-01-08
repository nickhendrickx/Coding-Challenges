def minMeetingRooms(self, intervals):
        intervals.sort()
        heap = [intervals[0][1]]

        for i in range(1,len(intervals)):
            start = intervals[i][0]
            if start >= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap,intervals[i][1])

        return len(heap)