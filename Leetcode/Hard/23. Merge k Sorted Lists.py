k = len(lists)

        # create a minheap of all the leftmost values. It will be helpful to also store the index 
        # in the heap so that we can get the node of that value. 
        # (We can't store the node in the heap to do this, because 
        # Python would try comparing nodes which isn't allowed)

        heap = [(lists[k0].val, k0, lists[k0]) for k0 in range(k) if lists[k0] is not None]
        
        
        heapq.heapify(heap)

        mergedhead = ListNode()
        merged = mergedhead

        while heap:
            val, index, node = heapq.heappop(heap)
            merged.next = node
            merged = node

            # if the array we popped from has a next element, add that to the heap of heap values
            if node.next:
                heapq.heappush(heap, (node.next.val, index,node.next))

        
        return mergedhead.next