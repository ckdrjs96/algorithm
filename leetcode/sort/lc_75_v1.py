#삽입정렬
#세가지 숫자만 있을땐 다른 방법보다 느림
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=1
        while i<len(nums):
            j=i
            while j>0 and nums[j-1]>nums[j]:
                nums[j-1],nums[j]=nums[j],nums[j-1]
                j-=1
            i+=1
            print(nums)