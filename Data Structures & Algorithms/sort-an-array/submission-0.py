class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(start, mid, end):
            temp = []
            idx1 = start
            idx2 = mid+1
            while idx1 <= mid and idx2 <= end:
                if nums[idx2] < nums[idx1]:
                    temp.append(nums[idx2])
                    idx2 += 1
                else:
                    temp.append(nums[idx1])
                    idx1 += 1
            while idx1 <= mid:
                temp.append(nums[idx1])
                idx1 += 1
            while idx2 <= end:
                temp.append(nums[idx2])
                idx2 += 1
            
            nums[start:end+1] = temp
        
        def mergeSort(start, end):
            if start == end:
                return
            mid = (start + end)//2
            mergeSort(start, mid)
            mergeSort(mid+1, end)
            merge(start, mid, end)
        
        n = len(nums)
        mergeSort(0, n-1)
        return nums