#타겟이 존배할만한 열선택후 이진검색
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return True
            return False

        ans = False
        for nums in matrix:
            if nums[-1] >= target and nums[0] <= target:
                # print(nums)
                ans = search(nums)
            if ans:
                return True
        else:
            return False