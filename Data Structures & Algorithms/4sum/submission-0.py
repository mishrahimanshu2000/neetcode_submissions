class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        temp = []

        def twoSum(idx, target):
            start, end = idx, n-1
            while start < end:
                sm = nums[start] + nums[end]
                if sm < target:
                    start += 1
                elif sm > target:
                    end -= 1
                else:
                    ans.append(temp + [nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start+=1

        def kSum(k, idx, target):
            if k == 2:
                twoSum(idx, target)
                return
            for i in range(idx, n-k+1):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                kSum(k-1, i+1, target-nums[i])
                temp.pop()
        
        kSum(4, 0, target)
        return ans
