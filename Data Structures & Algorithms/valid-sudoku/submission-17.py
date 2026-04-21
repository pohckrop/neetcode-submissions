class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                cell = board[row][col]
                if cell != '.':
                    if cell in cols[col]:
                        return False
                    if cell in rows[row]:
                        return False
                    if cell in squares[row//3,col//3]:
                        return False
                    else:
                        rows[row].add(cell)
                        cols[col].add(cell)
                        squares[row//3,col//3].add(cell)
        
        print(cols)

        return True



        