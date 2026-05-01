class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        if k == n:
            return points
        
        heap = []
        def calculateDistance(x,y):
            return ((x - 0)**2 + (y - 0)**2) ** 0.5
        
        for x,y in points:
            dis = calculateDistance(x,y)
            heapq.heappush(heap, (-dis, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            _,x,y = heapq.heappop(heap)
            res.append([x,y])
        return res