class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        start = 0
        end = n-1
        ans = 0
        while start < end:
            max_h = min(heights[start], heights[end])
            ans = max(ans, (max_h * (end-start)))
            while start < end and heights[start] <= max_h:
                start += 1
            while start < end and heights[end] <= max_h:
                end -= 1
        return ans