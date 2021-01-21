
def runs(N,M,arr):
    max_sum = 0
    min_sum = sum(arr)
    for idx in range(N - M + 1):
        now = sum(arr[idx:idx+M])
        min_sum = min(now, min_sum)
        max_sum = max(max_sum, now)
    return max_sum- min_sum


T = int(input())
for test_case in range(1, T + 1):
    N, M= map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{test_case}',runs(N,M,arr))