class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            rowcount=[]
            for val in row:
                if val in rowcount:
                    print("row")
                    return False
                if val!=".":
                    rowcount.append(val)
                    

        for column in range(9):
            columncount=[]
            for row in board:
                
                if row[column] in columncount:
                    return False
                if row[column]!=".":
                    columncount.append(row[column])
                    print(columncount)
            
        

        for val in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (val//3) * 3 + i
                    col = (val%3) * 3 + j

                    square = board[row][col]
                    if square in seen:
                        print("box")
                        return False
                    if square != ".":
                        seen.add(square)
    
    
        return True
        