class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        while n:
            n =n&(n-1) #가장 낮은 비트를 하나씩 빼준다
            cnt+=1
        return cnt