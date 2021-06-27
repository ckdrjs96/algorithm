def solution(m, n, puddles):
    map=[[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if [j+1,i+1] in puddles:
                continue
            if i==0 and j==0:
                map[i][j]=1
            elif i==0:
                map[i][j]=map[i][j-1]
            elif j==0:
                map[i][j]=map[i-1][j]
            else:
                map[i][j]=map[i-1][j]+map[i][j-1]
        # print(map)
    return map[n-1][m-1]%1000000007
