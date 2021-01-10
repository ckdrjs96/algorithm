def bus(k,n,m,arr):
    start=0
    cnt=0
    while start<n:
        stop=start+k

        if stop>=n:
            break

        for i in arr[::-1]:
            if start<i<=stop:
                start=i
                cnt+=1
                break
        else:
            return 0
    return cnt

#T=1
T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans=bus(K,N,M, arr)
    print(f'#{test_case}',ans)