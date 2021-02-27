#Dynamic Programming
#T=1
T =int(input())
for test_case in range(1, T + 1):
    N= int(input())

    memo=[0,1,3,6]
    for i in range(4,N+1):
        memo.append(memo[i-1]+2*memo[i-2]+memo[i-3])

    print(f'#{test_case}', memo[N])
