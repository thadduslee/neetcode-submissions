class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res, sol = [], []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(sol[:]))
                return
            
            digit = digits[i]
            for ch in digitToChar[digit]:
                sol.append(ch)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)
        return res
