def find_group(graph):
    visitied =[[False]*N for _ in range(N)]
    s_y,s_x =-1,-1
    max_cnt = -1
    rainbow_max = -1
    for i in range(N):
        for j in range(N):
            if graph[i][j] >0 and not visitied[i][j]:
                stack = [[i,j]]
                cnt = 1
                block_num = graph[i][j]
                rainbow = []
                visitied[i][j] = True
                while stack:
                    y,x = stack.pop()
                    for dy, dx in moves:
                        ny = y+dy
                        nx = x+dx
                        if 0<= ny <N and 0<= nx <N and (graph[ny][nx] ==block_num or graph[ny][nx] ==0) and not visitied[ny][nx]:
                            stack.append([ny,nx])
                            cnt+=1
                            visitied[ny][nx] = True
                            if graph[ny][nx] ==0:

                                rainbow.append([ny,nx])
                for rain_y,rain_x in rainbow:
                    visitied[rain_y][rain_x] = False
                rainbow_cnt = len(rainbow)
                if cnt > max_cnt or (cnt == max_cnt and rainbow_cnt >= rainbow_max):
                    s_y,s_x,max_cnt = i,j,cnt
                    rainbow_max = rainbow_cnt
    #                 print(s_y,s_x,max_cnt)
    # print('-----')
    return s_y,s_x,max_cnt

def gravity(graph):
    for i in range(N):
        e_p=-1
        for j in range(N-1,-1,-1):
            # print(e_p)
            if graph[j][i] ==-2:
                e_p = max(e_p,j)
            elif graph[j][i] >=0 and e_p!=-1:
                graph[e_p][i] = graph[j][i]
                graph[j][i] = -2
                e_p-=1
            elif graph[j][i] == -1:
                e_p = -1
    return graph



N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
moves = [[1,0],[0,1],[-1,0],[0,-1]]
# for boar in board:
#     print(boar)
score = 0
while True:
    #1
    i,j,max_cnt = find_group(board)
    if max_cnt <2:
        break
    # print(i,j,max_cnt)
    #2
    score += max_cnt**2
    # print(score,max_cnt**2)
    stack = [[i, j]]
    block_num = board[i][j]
    while stack:
        y, x = stack.pop()
        for dy, dx in moves:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and (board[ny][nx] == block_num or board[ny][nx] == 0):
                stack.append([ny, nx])
                board[ny][nx] = -2

    #3
    board = gravity(board)
    # print('gravity1')
    # for boar in board:
    #     print(boar)
    #4
    new_board = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N-1-i][j] = board[j][i]
    board = new_board
    # print('turn')
    # for boar in board:
    #     print(boar)

    #5
    board = gravity(board)
    # print('gravity2')
    # for boar in board:
    #     print(boar)

print(score)



