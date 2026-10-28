class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            for j in range(9):
                digit = board[i][j]
                if digit in row:
                    return False
                elif digit != '.':
                    row.add(digit)
        
        for i in range(9):
            col = set()
            for j in range(9):
                value = board[j][i]
                if value in col:
                    return False
                elif value != '.':
                    col.add(value)
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = set()
                for x in range(3):
                    for y in range(3):
                        value = board[i+x][j+y]
                        if value in box:
                            return False
                        elif value != '.':
                            box.add(value)
        return True
                    

                