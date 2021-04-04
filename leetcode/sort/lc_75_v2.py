#세가지 색만있을떈 가운데 색을 기준으로 스왑하면서 정렬
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1

            elif nums[white] > 1:
                blue -= 1
                nums[blue], nums[white] = nums[white], nums[blue]

            else:
                white += 1
