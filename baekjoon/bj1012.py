import sys
sys.setrecursionlimit(10000)

def dfs(x,y,m,n):
    if x < 0 or x >= m or y < 0 or y >= n or board[y][x]!= 1:
        return
    board[y][x] = 0
    check_point = [[x + 1, y], [x, y + 1], [x - 1, y], [x, y - 1]]
    for x,y in check_point:
        dfs(x,y,m,n)

trial=int(input())
for _ in range(trial):
    m,n,k = map(int, input().split())
    board=[[0]*m for _ in range(n)]
    count=0
    for i in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                dfs(j,i,m,n)
                count+=1
    print(count)