class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []
        q = deque()
        for v in freq.values():
            heap.append(-v)
        heapq.heapify(heap)
        time = 0
        while heap or q:
            if heap:
                task = heapq.heappop(heap)
                task += 1
                if task < 0:
                    q.append((time+n+1,task))
            time += 1
            if q and q[0][0] <= time:
                heapq.heappush(heap, q.popleft()[1])
        
        return time
                