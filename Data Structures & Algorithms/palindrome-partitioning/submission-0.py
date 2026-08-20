class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []

        def is_palindrome(string):
            if string == string[::-1]:
                return True
            return False

        def backtrack(index):
            if index == len(s):
                res.append(sol[:])
                return
            
            for end in range(index+1, len(s)+1):
                if is_palindrome(s[index:end]):
                    sol.append(s[index:end])
                    backtrack(end)
                    sol.pop()
        backtrack(0)
        return res
