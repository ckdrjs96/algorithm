import sys
N=int(input())
K=int(input())
input = sys.stdin.readline
board=[[0]*N for _ in range(N)]
for _ in range(K):
    y,x=map(int, input().rstrip().split())
    board[y-1][x-1] = 1

apple = [list() for _ in range(K)]
L=int(input())

change=dict()
for _ in range(L):
    t,val=input().rstrip().split()
    change[int(t)] = val

def direct(dy,dx,val):
    right=[[0,1],[1,0],[0,-1],[-1,0]]
    left = [[0,1],[-1,0],[0,-1],[1,0]]
    if val=='D':
        idx=right.index([dy,dx])
        return right[(idx+1)%4]
    elif val=='L':
        idx=left.index([dy,dx])
        return left[(idx+1)%4]

board[0][0] = 2
time=0
y,x=0,0
# t_y,t_x =0,0
dy,dx = 0,1
snail = [[y,x]]
while True:
    # print(time)
    # for bor in board:
    #     print(bor)

    if time in change:
        # print('chage')
        dy,dx = direct(dy,dx,change[time])
    y,x=y+dy,x+dx
    time += 1
    #벽에 부딫 경우
    if y<0 or y>=N or x<0 or x>=N:
        print(time)
        break
    #사과를 먹는 경우
    elif board[y][x] == 1:
        board[y][x] = 2
        snail.append([y,x])

    #자기 몸에 닿는 경우
    elif board[y][x] == 2:
        print(time)
        break
    #그냥 빈칸일경우
    else:
        board[y][x] = 2
        t_y,t_x=snail.pop(0)
        snail.append([y,x])
        board[t_y][t_x] = 0



