class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        columns = len(board[0])

        def capture(i,j):
            if i < 0 or i >= rows or j < 0 or j >= columns or board[i][j] != "O":
                return

            board[i][j] = "Temp"
            capture(i+1,j)
            capture(i,j+1)
            capture(i-1,j)
            capture(i,j-1)
        
        for i in range(rows):
            if board[i][0] == "O":
                capture(i,0)
            
            if board[i][columns-1] == "O":
                capture(i,columns-1)
        
        for j in range(columns):
            if board[0][j] == "O":
                capture(0,j)
            
            if board[rows-1][j] == "O":
                capture(rows-1,j)
        
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == "Temp":
                    board[i][j] = "O"
                
                elif board[i][j] == "O":
                    board[i][j] = "X"
            

        

        

        

            
            

