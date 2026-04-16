class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = r_max = 0 
        l = 0
        r = n-1
        ans = 0
        while l < r:
            if height[l] <= height[r]:
                if l_max > height[l]:
                    ans += l_max - height[l]
                else:
                    l_max = height[l]
                l += 1
            else:
                if r_max > height[r]:
                    ans += r_max - height[r]
                else:
                    r_max = height[r]
                r -= 1
        return ans