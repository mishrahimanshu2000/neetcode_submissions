class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        def twoSum(idx, target):
            start = idx
            end = n-1
            while start < end:
                sm = nums[start] + nums[end]
                if sm == target:
                    ans.append([-target, nums[start], nums[end]])
                    start+=1
                    end-=1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif sm < target:
                    start+=1
                else:
                    end -= 1
        for i,num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            twoSum(i+1, -num)
        return ans
