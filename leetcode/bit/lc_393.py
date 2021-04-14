class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 뒤에 n바이트들이 10으로 시작하는지 확인
        def check(n):
            for i in range(start + 1, start + n + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            first = data[start]
            # 4바이트 확인
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            # 3바이트 확인
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            # 2바이트 확인
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            # 1바이트 확인
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True