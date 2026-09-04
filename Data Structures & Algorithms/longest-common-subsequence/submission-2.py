class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        len1 = len(text1)
        len2 = len(text2)

        def helper(i,j):
            if i == len1 or j == len2:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + helper(i+1,j+1)
                
            else:
                memo[(i,j)] = max(helper(i+1, j), helper(i,j+1))
            return memo[(i,j)]
        return helper(0,0)