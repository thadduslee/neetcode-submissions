class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        path = set()
        def backtrack(r, c, index):
            if index == len(word):
                return True
            
            elif r >= rows or c >= columns or r < 0 or c < 0 or board[r][c] != word[index] or (r,c) in path:
                return False
            
            path.add((r,c))
            res = (backtrack(r+1,c, index+1) or
                backtrack(r, c+1, index+1) or
                backtrack(r-1, c, index+1) or 
                backtrack(r, c-1, index+1))
            path.remove((r,c))
            return res

        for i in range(rows):
            for j in range(columns):
                if backtrack(i, j, 0):
                    return True
        return False
                        
            
