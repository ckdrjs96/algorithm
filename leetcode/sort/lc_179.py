class Solution:
    def compare(self, a, b):
        if str(a) + str(b) < str(b) + str(a):
            return True
        return False

    def largestNumber(self, nums: List[int]) -> str:
        # 삽입된위치부터 정렬하면서 앞으로 가기
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.compare(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1
            print(nums)
        return str(int(''.join(map(str, nums))))
