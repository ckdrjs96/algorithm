## 비트연산자를 이용하여 부분집합 만들기

def make_subset(N,K):
    arr = range(1, 13)
    n = len(arr)
    ans = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                #부분집합만들기
                subset.append(arr[j])

        #조건에 맞으면 정답으로
        if len(subset) == N and sum(subset) == K:
            ans.append(subset)
    print(ans)
    return ans


T=1
#T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    print(f'#{test_case}',len(make_subset(N,K)))


