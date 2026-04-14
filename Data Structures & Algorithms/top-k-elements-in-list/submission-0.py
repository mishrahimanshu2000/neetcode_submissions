class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key,v in freq.items():
            heapq.heappush(heap, (v, key))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        while heap:
            v, key = heapq.heappop(heap)
            ans.append(key)
        return ans 