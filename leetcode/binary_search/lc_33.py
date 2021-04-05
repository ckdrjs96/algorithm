class Solution:
    idx=0
    def search(self, nums: List[int], target: int) -> int:
        def search2(nums: List[int], target: int) -> int:

            n = len(nums)
            if n == 0:
                self.idx = -1
                return self.idx
            half = n // 2
            # print(nums,self.idx,half)
            if nums[half] == target:
                self.idx += half
                # print(self.idx)
                return self.idx

            elif nums[half] < target:
                self.idx += half + 1
                self.search(nums[half + 1:], target)

            else:
                self.search(nums[:half], target)

            return self.idx

        n = len(nums)
        i = 0
        while nums[i] > nums[n - i - 1]:
            i += 1
        if nums[i] > nums[n - i]:
            i = n - i

        print(i)
        new_nums=nums[i:]+nums[:i]
        p_idx=search2(nums,target)

