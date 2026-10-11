class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        path = set()

        def backtrack(i,j,index):
            if index == len(word):
                return True
            
            if i < 0 or i == rows or j < 0 or j == columns or board[i][j] != word[index] or (i,j) in path:
                return False
            
            path.add((i,j))
            results = (backtrack(i+1,j,index+1) or 
            backtrack(i,j+1, index+1) or
            backtrack(i-1,j,index+1) or
            backtrack(i,j-1, index+1))

            path.remove((i,j))
            return results
        for row in range(rows):
            for column in range(columns):
                if backtrack(row,column,0):
                    return True
        
        return False
        

                        
            
