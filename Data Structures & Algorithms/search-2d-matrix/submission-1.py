class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def findRow(target):
            start = 0
            end = m-1
            while start <= end:
                mid = start+(end-start)//2
                if matrix[mid][0] <= target and matrix[mid][n-1] >= target:
                    return mid
                elif matrix[mid][n-1] < target:
                    start = mid+1
                else:
                    end = mid-1
            
            return -1
        
        row = findRow(target)

        if row == -1:
            return False
        
        start = 0
        end = n-1
        while start <= end:
            mid = start + (end-start)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid+1
            else:
                end = mid-1
            
        return False

