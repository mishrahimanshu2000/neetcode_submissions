class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0],cost[1])
        
        last = 0
        s_last = 0
        curr = 0
        for i in range(2,n+1):
            curr = min(last+cost[i-1], cost[i-2]+s_last)
            s_last = last
            last = curr
        return curr