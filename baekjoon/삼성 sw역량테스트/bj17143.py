import sys
def move(r,c,s,d,z):

    # print(r,c,s,d,z)
    if d==1 or d==4:
        dir = -1
    else: dir =1

    if d==1 or d==2:
        s = s%((R-1)*2)
        for i in range(s):
            if r==R:
                dir = -1
            elif r == 1:
                dir = 1
            r += dir

        if dir ==1:
            d=2
        else: d=1

    elif d==3 or d==4:
        s = s % ((C - 1) * 2)
        for i in range(s):
            if c==C:
                dir = -1
            elif c == 1:
                dir = 1
            c += dir
            # print(c)
        if dir ==1:
            d=3
        else: d=4

    return r,c,s,d,z

input = sys.stdin.readline
R,C,M = map(int, input().split())
board = [[[0,0,0] for _ in range(C+1)] for _ in range(R+1)]
for _ in range(M):
    a,b,s,d,z = map(int,input().split())
    board[a][b] = [s,d,z]

# print(board)
ans = 0
for c in range(1,C+1):
    #2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    for r in range(1,R+1):
        if board[r][c] != [0,0,0]:
            ans += board[r][c][2]
            board[r][c] = [0,0,0]
            break
    #3 상어가 이동한다.
    new_board = [[[0, 0, 0] for _ in range(C + 1)] for _ in range(R + 1)]
    for i in range(R+1):
        for j in range(C+1):
            if board[i][j] !=[0,0,0]:
                r, c, s, d, z = move(i,j,*board[i][j])
                if new_board[r][c] == [0,0,0]:
                    new_board[r][c] = [s,d,z]
                else:
                    if new_board[r][c][2] <z:
                        new_board[r][c] = [s,d,z]
    board = new_board

print(ans)
