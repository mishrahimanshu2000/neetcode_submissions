class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        ele1 = ele2 = float('-inf')
        cnt1 = cnt2 = 0
        for i in range(n):
            num = nums[i]
            if ele1 == num:
                cnt1+=1
            elif ele2 == num:
                cnt2+=1
            elif cnt1 == 0:
                ele1 = num
                cnt1 = 1
            elif cnt2 == 0:
                ele2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
            
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == ele1:
                cnt1+=1
            if num == ele2:
                cnt2+=1
        
        ans = []
        if cnt1 > n//3:
            ans.append(ele1)
        if ele1 != ele2 and cnt2 > n//3:
            ans.append(ele2)
        
        return ans