#T=1
T =int(input())
for test_case in range(1, T + 1):
    n,a,b = map(int, input().split())
    B= [[-1]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,b)+1):
            if j==0 or i==j:
                B[i][j]=1

            else:
                B[i][j]=B[i-1][j-1]+B[i-1][j]

    print(f'#{test_case}',B[n][b])

