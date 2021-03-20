#정답
M,N=list(map(int,input().split()))
graph=[list(map(int,input().split())) for _ in range(N)]

cost=[[0]*M for _ in range(N)]
cost[0][0]=graph[0][0]
for i in range(N):
    for j in range(M):
        if i==0 and j>1:
            cost[i][j]=cost[i][j-1]+graph[i][j]
        cost[i][j]=max(cost[i-1][j],cost[i][j-1])+graph[i][j]
print(cost[-1][-1])
