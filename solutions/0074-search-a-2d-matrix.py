# pretty chill binary search with some careful indexing on the row / col to avoid out of range errors

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        rowCount = len(matrix)
        colCount = len(matrix[0])
        size = rowCount * colCount

        left, right = 0, size - 1
        while left <= right:
            mid = left + (right - left) // 2
            midRow = mid // colCount
            midCol = mid % colCount
            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False
