def find_warmhole(board):
    warmhole_left = [(-1,-1) for _ in range(5)]
    warmhole_right = [(-1, -1) for _ in range(5)]
    for i in range(N):
        for j in range(N):
            if board[i][j] >5:
                num = board[i][j]-6
                if warmhole_left[num] == (-1,-1):
                    warmhole_left[num] = (i,j)
                else:
                    warmhole_right[num] = (i, j)
    warm_dict = dict()
    for i in range(5):
        warm_dict[warmhole_right[i]] = warmhole_left[i]
        warm_dict[warmhole_left[i]] = warmhole_right[i]
    warm_dict.update(dict(zip(warmhole_right,warmhole_left)))
    return warm_dict


def start(s_y,s_x,dir):
    stop_y,stop_x=s_y,s_x
    cnt = 0
    while True:
        #print(s_y,s_x,dir,cnt)
        dy,dx = moves[dir]
        n_y=s_y+dy
        n_x=s_x+dx
        if n_y<0 or n_y>=N or n_x<0 or n_x>=N:
            dir=opposite_dict[dir]
            cnt+=1
            s_x, s_y = n_x, n_y
        elif board[n_y][n_x] == -1 or (stop_x==n_x and stop_y==n_y):
            return cnt
        elif board[n_y][n_x] == 5:
            dir=opposite_dict[dir]
            cnt+=1
            s_x, s_y = n_x, n_y
        elif board[n_y][n_x] == 0:
            s_x,s_y=n_x,n_y
        elif board[n_y][n_x] <5:
            block_dict = blocks[board[n_y][n_x]]
            dir = block_dict[dir]
            s_x, s_y = n_x, n_y
            cnt+=1
        elif board[n_y][n_x] >5:
            s_y,s_x= warmhole[(n_y,n_x)]




T = int(input())
# T=1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    moves = [[-1,0],[1,0],[0,1],[0,-1]] #up,down,right,left
    opposite_dict = {0:1,1:0,2:3,3:2}
    blocks ={1:{0:1,1:2,2:3,3:0},2:{0:2,1:0,2:3,3:1},3:{0:3,1:0,2:1,3:2},4:{0:1,1:3,2:0,3:2}}
    warmhole = find_warmhole(board)
    #print(warmhole)
    max_ans=0
    # start(2,3,2)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for k in range(4):
                    ans = start(i,j,k)
                    #print('next')

                    max_ans = max(ans,max_ans)
    print(f'#{test_case} {max_ans}')