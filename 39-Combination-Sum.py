class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        
        def dfs(i, sub, total):
            if i>=len(candidates):
                return

            if total < target:
                sub.append(candidates[i])
                dfs(i, sub, total + candidates[i])
                sub.pop()
                dfs(i+1, sub, total)
            elif total > target:
                return
            else:
                res.append(sub.copy())
                return

        dfs(0,sub, 0)
        return res