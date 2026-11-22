class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix) * len(matrix[0]))-1

        def pos_to_rc(i):
            row = i//len(matrix[0])
            column = i % len(matrix[0]) 
            return row, column 

        while l<=r:
            mid = (l+r)//2
            mid_row, mid_column = pos_to_rc(mid)
            val = matrix[mid_row][mid_column]
            if target == val:
                return True
            elif target > val:
                l = mid + 1
            else:
                r = mid - 1
        
        return False