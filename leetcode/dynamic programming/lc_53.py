# 앞에서부터 더해서 0보다 작으면 버리고 다시
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        add = 0
        ans = -float('inf')
        for val in nums:
            add += val
            if add > ans:
                ans = add
            if add < 0:
                add = 0

        return ans