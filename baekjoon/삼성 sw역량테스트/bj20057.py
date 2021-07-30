import sys

def check(y,x,val):
    global remain,out

    if 0<=y<N and 0<=x<N:
        board[y][x] +=val
        remain += val
    else:
        out += val
def sand_move(s_y,s_x,dy,dx):
    global remain,out
    remain, out = 0, 0
    sand = board[s_y][s_x]
    board[s_y][s_x] =0
    check(s_y+2*dy,s_x+2*dx,int(sand*0.05))

    check(s_y+2*dx,s_x+2*dy, int(sand*0.02))
    check(s_y-2*dx,s_x-2*dy, int(sand*0.02))

    check(s_y + dx, s_x + dy, int(sand * 0.07))
    check(s_y - dx, s_x - dy, int(sand * 0.07))

    check(s_y +dy + 1*dx,s_x + dx +1*dy, int(sand * 0.1))
    check(s_y +dy - 1*dx,s_x + dx -1*dy, int(sand * 0.1))

    check(s_y - dy + 1*dx,s_x - dx + 1*dy, int(sand * 0.01))
    check(s_y - dy - 1*dx,s_x - dx - 1*dy, int(sand * 0.01))

    check(s_y+dy,s_x+dx, sand - remain - out)
    return out


N = int(input())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
s_x,s_y=N//2,N//2
how_moves={0:[0,-1], 1:[1,0], 2:[0,1], 3:[-1,0]}
dir_num=0
length =1
change_cnt=0
stop =False
sand_out = 0
while True:
    dy = how_moves[dir_num][0]
    dx = how_moves[dir_num][1]
    for i in range(length):
        s_x +=dx
        s_y +=dy
        # print(s_y, s_x)

        sand_out += sand_move(s_y,s_x,dy,dx)
        # print(sand_out)
        # for boar in board:
        #     print(boar)
        if s_x ==0 and s_y ==0:
            stop =True
            break

    if stop:
        break
    dir_num=(dir_num+1)%4
    change_cnt+=1
    if change_cnt%2 ==0:
        length+=1
print(sand_out)