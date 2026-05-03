class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
    # 1. Sort to handle duplicates and enable early exit
        candidates.sort()
    
        def backtrack(remain, stack, start):
            if remain == 0:
                # Found a valid combination
                results.append(list(stack))
                return
            
            for i in range(start, len(candidates)):
                # 2. Skip duplicates: 
                # If the current number is same as previous AND it's not the 
                # first element in this recursive branch, skip it.
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                    
                # 3. Early Exit:
                # If current number exceeds remaining sum, no point looking further
                if candidates[i] > remain:
                    break
                    
                stack.append(candidates[i])
                # Move to i + 1 because we cannot reuse the same element
                backtrack(remain - candidates[i], stack, i + 1)
                stack.pop() # Backtrack

        backtrack(target, [], 0)
        return results