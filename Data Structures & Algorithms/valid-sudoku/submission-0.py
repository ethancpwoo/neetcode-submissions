class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = [{} for row in range(9)]
        column_map = [{} for row in range(9)]
        square_map = [{} for row in range(9)]
        
        for row in range(len(board)):
            for column in range(len(board)):
                num = board[row][column] 
                if num == '.': 
                    continue 
                num = int(num)
                square = (int(row/3) * 3) + int(column/3)
                print(f"num: {num}, square: {square}")
                if num in row_map[row]:
                    print(f"row: {row} num: {num}")
                    return False
                if num in column_map[column]:
                    print(f"column: {column} num: {num}")
                    return False
                if num in square_map[square]:
                    print(f"square: {column} num: {num}")
                    return False
                row_map[row][num] = 1
                column_map[column][num] = 1
                square_map[square][num] = 1
        return True        
        