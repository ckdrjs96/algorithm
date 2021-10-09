from copy import deepcopy

def transpose(board):
    for i in range(n):
        for j in range(i+1,n):
            board[i][j], board[j][i] = board[j][i],board[i][j]
    return board

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
#dir 0:left 1:right 2:up 3:down
def moves(n_board,dir):
    board = deepcopy(n_board)
    #어느 방향이든 뒤집어서 우 ->좌 로 움직이게 만들기
    if dir == 2 or dir ==3:
        board = transpose(board)

    for i in range(n):
        if dir ==0 or dir == 2:
            now = board[i]
        else:
            now = board[i][::-1]
        for j in range(n):
            # ex) [0,0,2,2] - > [2,2,0,0] 으로 만들기 (합치는거는 밑에 while문)
            if now[j] == 0:
                point = j+1
                while point <n:
                    if now[point] ==0:
                        point +=1 
                    else:
                        now[j:] = now[point:]+[0]*(point-j)
                        break
            point = j+1
            while point<n:
                if now[point] == 0:
                    point +=1
                elif now[point] == now[j]:
                    now[j] = 2*now[j]
                    now[j+1:] = now[point+1:] +[0]*(point-j)
                    break
                else:
                    now[j+1:] = now[point:] +[0]*(point-j-1)
                    break
            
        if dir ==0 or dir == 2:
            board[i]=now
        else:
            board[i]=now[::-1]

    if dir == 2 or dir ==3:
        board = transpose(board)

    return board


def dfs(board,cnt):
    global ans
    if cnt ==5:
        for i in range(n):
            ans = max(ans, max(board[i]))
        #max(board) 하면 일차원리스트의 합이 가장큰 리스트가 나온다
        return
        
    for dir in range(4):
        board2 = moves(board,dir)
        dfs(board2,cnt+1)

global ans
ans = 0
dfs(graph,0)

print(ans)