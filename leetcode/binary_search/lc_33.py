class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 최솟값 위치 찾기
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        nums = nums[left:] + nums[:left]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # overflow 방지
            # mid_pivot=(mid+pivot) % len(nums) #리스트 변화주지말고 mid값을 회전시키면서 판별가능
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                #아래 분기를 간소화 가능 return (mid+pivot) %len(nums)
                if mid < len(nums) - pivot:
                    return pivot + mid
                else:
                    return mid - len(nums) + pivot
        return -1

