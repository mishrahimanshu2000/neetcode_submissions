class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heapq.heappush(heap, -num)
        
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            if a == b:
                continue
            else:
                rem = a - b
                heapq.heappush(heap, rem)
            
        if heap:
            return -heap[0]
        return 0
