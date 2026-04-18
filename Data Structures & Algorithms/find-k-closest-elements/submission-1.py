class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = 0
        r = len(arr)-1
        # binary search for the closest value to x
        while l < r:
            m = l + (r-l)//2
            if arr[m] < x:
                l = m + 1
            else:
                r = m
        # Initialize the pointer to expand the window
        r = l
        l = l-1
        # while this window becomes of valid size
        while r-l-1 < k:
            if l < 0:
                r += 1
            elif r >= n:
                l-=1
            elif abs(x-arr[l]) <= abs(x-arr[r]):
                l -= 1
            else:
                r += 1
        return arr[l+1:r]
        
