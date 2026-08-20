class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dfs(nums, alice, bob, turn):
            if len(nums) == 0:
                if alice > bob:
                    return True
                return False
            
            if turn == "a":
                return dfs(nums[1:], alice + nums[0], bob, "b") or dfs(nums[:-1], alice + nums[-1], bob, "b")
            
            elif turn == "b":
                return dfs(nums[1:], alice, bob + nums[0], "a") or dfs(nums[:-1], alice, bob + nums[-1], "a")
            
        return dfs(piles, 0,0, "a")
            

            
            