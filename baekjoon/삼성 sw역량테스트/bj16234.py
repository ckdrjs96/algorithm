import sys
N, L, R = map(int,input().split())
input = sys.stdin.readline
board = [list(map(int,input().rstrip().split())) for _ in range(N)]

moves=[[1,0],[-1,0],[0,1],[0,-1]]

def one_group(q):
    group = []
    group_sum = 0
    visited[q[0][0]][q[0][1]] = True
    while q:
        y,x = q.pop()
        group.append([y,x])
        group_sum+=board[y][x]
        for dy, dx in moves:
            if 0<= y+dy <N and 0<=x+dx<N and not visited[y+dy][x+dx]:
                if L<=abs(board[y][x]-board[y+dy][x+dx]) <=R:
                    q.append([y+dy,x+dx])
                    visited[y+dy][x+dx] = True

    return group, group_sum

cnt =0
while True:
    visited = [[False] * N for _ in range(N)]
    stop = True
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                group, group_sum = one_group([[i,j]])
                if len(group) > 1:
                    stop = False
                    for y, x in group:
                        board[y][x] = group_sum // len(group)

    if stop:
        print(cnt)
        break
    cnt += 1



