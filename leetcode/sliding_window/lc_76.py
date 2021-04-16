class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        right = 0

        # 오른쪽이동
        while right < len(s):
            missing -= t_cnt[s[right]] > 0  # True면 1빼기
            t_cnt[s[right]] -= 1
            right += 1

            if missing == 0:
                # 왼쪽이동
                while left < right and t_cnt[s[left]] < 0:
                    t_cnt[s[left]] += 1
                    left += 1

                # 작은길이면 저장
                if not end or right - left <= end - start:
                    start, end = left, right
                    t_cnt[s[left]] += 1
                    missing += 1
                    left += 1

        return s[start:end]