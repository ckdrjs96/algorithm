import sys
def next_location(y,x,watch_d):
    # 1 현재 위치를 청소한다
    board[y][x] = 2
    cnt = 0
    # 2 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다
    while cnt<4:
        dy, dx = directions[(watch_d + 3) % 4]
        ny, nx = y + dy, x + dx
        watch_d = (watch_d + 3) % 4
        #a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        if board[ny][nx] == 0:
            return ny, nx,watch_d,1
        #b 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        else:
            cnt +=1
    dy, dx = directions[(watch_d + 2) % 4]
    ny, nx = y + dy, x + dx
    #d . 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
    if board[ny][nx] == 1:
        return -1,-1,-1,0
    #c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    else:
        return ny,nx,watch_d,0




n,m = map(int,input().split())
s_y,s_x, watch_d = map(int,input().split())
input = sys.stdin.readline
board = [list(map(int,input().split())) for _ in  range(n)]
directions = [[-1,0],[0,1],[1,0],[0,-1]]

ans = 1
while watch_d != -1:
    s_y, s_x, watch_d,move = next_location(s_y, s_x,watch_d)
    ans += move
print(ans)




