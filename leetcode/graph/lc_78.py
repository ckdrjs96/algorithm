#풀이보다 탐색할때마다 ans에 저장이 더 효율적
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.append([])

        ans = []
        group = []

        def dfs(val, start):
            if val == []:
                ans.append(group[:])
                return

            for idx, val in enumerate(nums[start:]):
                if val != []:
                    group.append(val)
                    dfs(val, start + idx + 1)
                    group.pop()
                else:
                    dfs(val, start + idx + 1)

        dfs(1, 0)
        return ans