class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        group = []

        def dfs(sub_target, start):
            if sub_target == 0:
                ans.append(group[:])

            elif sub_target < 0:
                return

            for idx, val in enumerate(candidates[start:]):
                group.append(val)
                dfs(sub_target - val, idx + start)
                group.pop()

        dfs(target, 0)
        return ans