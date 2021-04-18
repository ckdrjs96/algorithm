#최대 윈도우를 찾으면 그 윈도우를 유지시키면서 비교한다
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = -1
        count = collections.Counter()
        while right < len(s) - 1:
            right += 1
            count[s[right]] += 1
            print(left, right)
            print(s[left:right + 1])

            print('tt', sum(count.values()), max(count.values()))
            if right - left - max(count.values()) + 1 > k:
                count[s[left]] -= 1
                left += 1
                print(s[left:right])

        return right - left + 1 #윈도우의 크기를 반환(정답의 포인터 위치가 아니다)