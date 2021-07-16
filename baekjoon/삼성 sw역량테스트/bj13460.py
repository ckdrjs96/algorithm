import sys
input=sys.stdin.readline
N, M=map(int,input().rstrip().split())
board=[list(input().rstrip()) for _ in range(N)]
# visitied=[[False]*M for _ in range(N)]
visitied = [[[[False] * M for i in range(N)] for i in range(M)] for i in range(N)]
# board2=deepcopy(board)
def find(board,what):
    for i in range(N):
        for j in range(M):
            if board[i][j] == what:
                return i,j

def move(a,da,b,db):
    n=0
    while 0<=a+da<N and 0<=b+db<M and board[a+da][b+db]!='#':
        if board[a+da][b+db]=='O':
            return -1,-1, 0
        a,b = a+da, b+db
        n+=1
    return a,b,n



y,x=find(board,'R')
b_y,b_x = find(board,'B')


q=[[y,x,b_y,b_x]]
moves=[[1,0],[-1,0],[0,1],[0,-1]]
cnt=0
stop=False
visitied[y][x][b_y][b_x]=True
while q and cnt<10:
    q2=[]
    while q:
        y,x,b_y,b_x=q.pop()

        for boar in board:
            print(boar)
        print(y, x, b_y, b_x, cnt)
        for dy, dx in moves:
            new_y,new_x,nr= move(y,dy,x,dx)
            if new_y==-1 and new_x==-1:
                new_b_y, new_b_x,_ = move(b_y, dy, b_x, dx)
                #같이 따라 들어가면 무효
                if new_b_y==-1 and new_b_x ==-1:
                    continue
                else:
                    stop=True
                    break

            new_b_y,new_b_x, nb = move(b_y,dy,b_x,dx)
            if new_b_y==-1 and new_b_x ==-1:
                continue
            if new_y==new_b_y and new_x==new_b_x:
                if nr >nb:
                    new_y-=dy
                    new_x-=dx
                elif nr < nb:
                    new_b_y -=dy
                    new_b_x -= dx

            if not visitied[new_y][new_x][new_b_y][new_b_x]:
                visitied[new_y][new_x][new_b_y][new_b_x] = True
                q2.append([new_y, new_x, new_b_y, new_b_x])


    q=q2
    cnt+=1
    if stop:
        break

if not stop:
    cnt=-1
print(cnt)


