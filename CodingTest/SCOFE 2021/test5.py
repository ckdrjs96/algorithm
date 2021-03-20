#시간초과인것 같다.

def dfs(s_i,s_j):
    global cnt,min_cnt
    if cnt >= min_cnt:
        return
    print(s_i,s_j)
    if s_i==N-1:
        print(cnt)
        min_cnt=min(cnt,min_cnt)
        return
    for n,m in moves:
        i=s_i+n
        j=s_j+m

        if 0<=i<N and 0<=j<M:
            if graph[i][j]=='.':
                graph[i][j]='x'
                if n==0:
                    cnt+=1
                # print(i,j)
                dfs(i,j)
                graph[i][j]='.'
                if n==0:
                    cnt-=1


M,N=list(map(int,input().split()))
graph=[list(input()) for _ in range(N)]
moves=[[1,0],[0,1],[0,-1]]
# global cnt
cnt=0
min_cnt=float('inf')
for i in range(M):
    if graph[0][i]=='c':
        dfs(0,i)
        print('he',i)
if min_cnt==float('inf'):
    print(-1)
else:
    print(min_cnt)