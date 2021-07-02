#dfs시 시간초과
import sys
N,M = map(int,input().split())
board= [list(map(int,list(sys.stdin.readline().rstrip()))) for i in range(N)]

moves=[[1,0],[-1,0],[0,1],[0,-1]]
stack1=[[0,0]]

cnt=1
stop=False
while stack1:
    stack2 = []
    while stack1:
        x,y=stack1.pop()
        # board[y][x] = 0
        if x==M-1 and y==N-1:
            stop=True
            break
        for dx, dy in moves:
            if 0 <= x + dx < M and 0 <= y + dy < N and board[y + dy][x + dx] == 1:
                stack2.append([x + dx,y + dy])
                board[y + dy][x + dx] = 0
    if stop:
        break

    stack1=stack2.copy()
    cnt+=1
print(cnt)



