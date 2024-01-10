def findKthLargest(self, nums: List[int], k: int) -> int:
        x = [-num for num in nums]

        heapq.heapify(x)
        for _ in range(k):
            ret = heapq.heappop(x)

        return -ret