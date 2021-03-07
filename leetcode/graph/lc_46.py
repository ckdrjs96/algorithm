class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(remain):
            if len(remain) == 0:
                return
            ans = []
            for val in remain:
                next_list = dfs(list(set(remain) - set([val])))
                if next_list:
                    for next_val in next_list:
                        ans.append([val] + next_val)
                else:
                    ans.append([val])
            return ans

        return dfs(nums)