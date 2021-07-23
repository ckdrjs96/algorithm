import sys
from collections import defaultdict
drc = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def moves(y,x,s,dire):
    dire = dire%8
    dy, dx = drc[dire]
    y, x = (y + dy * s) % N, (x + dx * s) % N
    return y,x

def output():
    ans=0
    while fireballs:
        r,c = fireballs.pop()
        cnt,m,_,_ =board[r][c]
        if cnt ==1:
            ans+=m
        else:
            ans = ans + 4*(m//5)
    return ans

def show(x):
    for i in x:
        print(i)

N, M, K = map(int,input().split())
board = [[[0,0,0,0] for _ in range(N)] for _ in range(N)]
fireballs = []
for _ in range(M):
    r,c,m,s,d = map(int,sys.stdin.readline().split())
    board[r-1][c-1] = [1,m,s,d]
    fireballs.append([r-1,c-1])
# show(board)
# print(board,fireballs)
do=False
for time in range(K):
    # print()
    while fireballs:
        do = True
        fireballs2 = set()
        new_board = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]
        odd_even = defaultdict(int)
        while fireballs:
            r,c =fireballs.pop()
            cnt,m,s,d = board[r][c]
            if cnt ==1:
                new_r,new_c = moves(r,c,s,d)
                new_board[new_r][new_c][0] += 1
                new_board[new_r][new_c][1] += m
                new_board[new_r][new_c][2] += s

                if new_board[new_r][new_c][3] ==0:
                    new_board[new_r][new_c][3] += board[r][c][3]
                odd_even[(new_r,new_c)] += 1 if board[r][c][3] % 2 ==0 else -1
                fireballs2.add((new_r, new_c))

            elif cnt >1:
                s=s//cnt
                m=m//5
                if m==0:
                    continue

                if abs(before[(r,c)]) == cnt:
                    for k in range(4):
                        new_r, new_c = moves(r, c,s,2*k)
                        new_board[new_r][new_c][0] += 1
                        new_board[new_r][new_c][1] += m
                        new_board[new_r][new_c][2] += s

                        # if new_board[new_r][new_c][3] == 0:
                        new_board[new_r][new_c][3] = 2*k

                        odd_even[(new_r,new_c)]  += 1

                        fireballs2.add((new_r, new_c))
                else:
                    for k in range(4):
                        new_r, new_c = moves(r, c, s,2*k+1)
                        new_board[new_r][new_c][0] += 1
                        new_board[new_r][new_c][1] += m
                        new_board[new_r][new_c][2] += s
                        new_board[new_r][new_c][3] = 2 * k +1
                        odd_even[(new_r,new_c)] += -1
                        fireballs2.add((new_r, new_c))




    if do:
        fireballs=list(fireballs2)
        board=new_board
        before=odd_even
    # print(fireballs)
    # show(board)
    # show(before)


print(output())