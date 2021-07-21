import sys
N,M,H =map(int,input().split())
board = [[0] * (N-1) for _ in range(H)]
input=sys.stdin.readline
for _ in range(M):
    h,n=map(int,input().split())
    board[h-1][n-1] =1
    if n>1:
        board[h-1][n-2] = -1
    if n<N-1:
        board[h-1][n] = -1

def issame():
    for i in range(N):
        x=i
        for j in range(H):
            if x<N-1 and board[j][x] ==1:
                x+=1
            elif x>0 and board[j][x-1] == 1:
                x-=1
        if x != i:
            return False
    return True

def main(cnt,board,now,bi=0):
    global ans
    if ans >0:
        return

    for i in range(bi,H):
        for j in range(N-1):
            if board[i][j] == 0:
                board[i][j] = 1
                if issame():
                    ans = cnt
                    # print(cnt)
                    # print(board)
                    board[i][j] = 0
                    return
                elif cnt<now:
                    main(cnt+1,board,now,i)
                # print(board,i,j,cnt)
                board[i][j] = 0
global ans
ans =-1
# print(board)
if issame():
    ans=0
else:
    main(1,board,1)
    main(1, board, 2)
    main(1, board, 3)

print(ans)

