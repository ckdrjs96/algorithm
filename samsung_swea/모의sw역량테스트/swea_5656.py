
from copy import deepcopy
def bomb(graph,idx):
    stack = []
    board = deepcopy(graph)
    for i in range(H):
        if board[i][idx] !=0:
            stack.append([i,idx,board[i][idx]])
            break


    while stack:
        y,x,depth = stack.pop()
        for long in range(depth):
            for dy,dx in moves:
                ny = y+long*dy
                nx = x+long*dx
                if 0<=ny<H and 0<=nx<W and board[ny][nx] >0:
                    if board[ny][nx] !=1:
                        stack.append([ny,nx,board[ny][nx]])
                    board[ny][nx] = 0

    for i in range(W):
        change_y=H
        for j in range(H-1,-1,-1):
            if board[j][i] ==0 and change_y==H:
                change_y = j
            elif board[j][i] >0 and change_y <H:
                board[change_y][i] = board[j][i]
                board[j][i] = 0
                change_y -=1
    # for boar in board:
    #     print(boar)
    # print()
    return board

def dfs(cnt,board):
    global ans
    if cnt == N:
        remain = sum([boar.count(0) for boar in board])
        ans = max(ans,remain)
        return
    for i in range(W):
        new_board = bomb(board,i)
        dfs(cnt+1,new_board)

T = int(input())
global ans
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for test_case in range(1, T + 1):
    N,W,H = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(H)]
    ans = 0
    dfs(0,board)
    print(f'#{test_case} {W*H-ans}')



