#그냥 숫자개수로
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counts = collections.Counter(nums)
        for a, b in counts.items():
            if b > n // 2:
                return a
