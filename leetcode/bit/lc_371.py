#전가산기
#책보고 해결..
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFF
        int_max = 0x7FF

        while b != 0:
            # b:자리수올림
            # a:올림제외하고 더한값
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            print(a, b)

        if a > int_max:
            a = ~(a ^ mask)  # 음수의 2보수표현(a)을 다시 10진수 음수로 만들어주기
        return a
