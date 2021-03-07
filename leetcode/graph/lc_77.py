class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        group = []
        nums = [i for i in range(1, n + 1)]

        def dfs(remain, group):
            if len(group) == k:
                result.append(group[:])
                return

            for val in remain:
                next_list = [i for i in range(val + 1, n + 1)]
                group.append(val)
                dfs(next_list, group)
                group.pop()

        dfs(nums, group)
        return result