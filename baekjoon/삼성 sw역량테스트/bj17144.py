import sys
def spread():
    after = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if board[y][x] ==0:
                continue
            elif board[y][x] == -1:
                after[y][x] = -1
            else:
                cnt = 0
                for dy,dx in moves:
                    if 0<=y+dy<R and 0<=x+dx<C and board[y+dy][x+dx] != -1:
                        cnt+=1
                        after[y+dy][x+dx] += board[y][x]//5
                after[y][x] = after[y][x] + board[y][x] - (board[y][x]//5)*cnt
    return after

def up_rotate(air):
    for y in range(air-1,0,-1):
        board[y][0] =board[y-1][0]
    # for x in range(0,C-1):
    #     board[0][x] = board[0][x+1]
    board[0] = board[0][1:]+[0]
    for y in range(0,air):
        board[y][C-1] = board[y+1][C-1]
    # for x in range(C-1,1,-1):
    #     board[air][x] = board[air][x-1]
    board[air] = [-1,0] + board[air][1:-1]

def down_rotate(air):
    for y in range(air+1,R-1):
        board[y][0] = board[y+1][0]
    # for x in range(0,C-1):
    #     board[R-1][x] = board[R-1][x+1]
    board[R-1] = board[R-1][1:]+[0]
    for y in range(R-1,air,-1):
        board[y][C-1] = board[y-1][C-1]
    # for x in range(C-1,1,-1):
    #     board[air][x] = board[air][x-1]
    board[air] = [-1,0] + board[air][1:-1]


R, C, T=map(int,input().split())
input = sys.stdin.readline
board = [list(map(int,input().split())) for _ in range(R)]
airs=[]
for i in range(R):
    if board[i][0] == -1:
        airs.append(i)

moves =[[1,0],[-1,0],[0,1],[0,-1]]
for _ in range(T):
    board = spread()
    # print('spread')
    # for boar in board:
    #     print(boar)
    up_rotate(airs[0])
    down_rotate(airs[1])
    # print('all')
    # for boar in board:
    #     print(boar)
print(sum([sum(line) for line in board])+2)
