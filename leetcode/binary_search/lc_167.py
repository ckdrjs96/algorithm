class Solution:
    #two pointer
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        last = len(numbers) - 1
        while True:

            if numbers[start] + numbers[last] < target:
                start += 1
            elif numbers[start] + numbers[last] > target:
                last -= 1
            else:
                return [start + 1, last + 1]
    #두번쨰 풀이
    #binary search
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            left, right = k + 1, len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2  # overflow 방지
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1

