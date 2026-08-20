class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m = len(board)
        n = len(board[0])

        def capture(i,j):
            if (i < 0 or j < 0 or i >= m or j >= n or board[i][j] != "O"):
                return
            
            else:
                board[i][j] = "T"
                capture(i+1, j)
                capture(i, j+1)
                capture(i,j-1)
                capture(i-1, j)
        for i in range(m):
            if board[i][0] == "O":
                capture(i,0)
            if board[i][n-1] == "O":
                capture(i, n-1)
        
        for j in range(n):
            if board[0][j] == "O":
                capture(0,j)
            if board[m-1][j] == "O":
                capture(m-1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
            
        
