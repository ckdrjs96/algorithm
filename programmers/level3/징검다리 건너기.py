#이분 탐색
#stones가 200,000,000 이하이므로 twopointer 보다 이분탐색이 더 효율적 O(NlogK)
def solution(stones, k):
    left = 0
    right = max(stones)

    ans = float('inf')
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            # print(mid,cnt,stone)
            if stone - mid < 0:
                cnt += 1
                if cnt == k:
                    right = mid - 1
                    break
            else:
                cnt = 0

        else:
            ans = mid
            left = mid + 1

    return ans


# 채점 결과
# 정확성: 64.1
# 효율성: 33.3
# 합계: 97.4 / 100.0
# two pointer 효율성 13번만 통과 못함
def solution(stones, k):
    answer = 0
    left = 0
    right = k - 1

    ans = float('inf')
    while right < len(stones):
        stone_max = max(stones[left:right + 1])
        move = stones[left:right + 1].index(stone_max) + 1
        # print(left,right,move)
        left += move
        right += move

        ans = min(ans, stone_max)

    return ans