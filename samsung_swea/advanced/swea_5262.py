#DP algorithm O(n^2)
#T=1
T =int(input())
for test_case in range(1, T + 1):
    given = list(map(int, input().split()))
    LIS=[0]*len(given)
    for i in range(len(given)):
        LIS[i]=1
        for j in range(1,i):
            if given[j] < given[i] and 1+LIS[j] > LIS[i]:
                LIS[i]=1+LIS[j]
    print(f'#{test_case}',max(LIS))
