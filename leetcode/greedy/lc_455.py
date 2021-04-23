class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort(reverse=True)
        cnt = 0

        #작은값끼리 비교한다
        for child in g:
            while s:
                cookie = s.pop()
                if child <= cookie:
                    cnt += 1
                    break

            if not s:
                return cnt

        return cnt
