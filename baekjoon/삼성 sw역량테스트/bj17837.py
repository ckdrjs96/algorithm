def is_stop(stack):
    if len(stack)>=4:
        return True
    else: return False

def turn1():
    for i in range(1, K + 1):
        y, x, dir = horse[i]
        dy, dx = moves[dir]
        ny, nx = y + dy, x + dx
        # print(ny, nx)
        if ny < 0 or ny >= N or nx < 0 or nx >= N or color[ny][nx] == 2:
            dir = opposite_dict[dir]
            dy, dx = moves[dir]
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= N or nx < 0 or nx >= N or color[ny][nx] == 2:
                horse[i] = [y, x, dir]
            elif color[ny][nx] == 0:
                stack = board[y][x]
                idx = stack.index(i)
                board[y][x] = stack[:idx]
                if stack[idx:]:
                    board[ny][nx].extend(stack[idx:])
                    if is_stop(board[ny][nx]): return True
                for num in stack[idx:]:
                    if num == i:
                        horse[num] = [ny, nx, dir]
                    else:
                        horse[num] = [ny, nx, horse[num][2]]
            elif color[ny][nx] == 1:
                stack = board[y][x]
                idx = stack.index(i)
                board[y][x] = stack[:idx]
                if stack[idx:]:
                    board[ny][nx].extend(stack[idx:][::-1])
                    if is_stop(board[ny][nx]): return True
                for num in stack[idx:]:
                    if num == i:
                        horse[num] = [ny, nx, dir]
                    else:
                        horse[num] = [ny, nx, horse[num][2]]

        elif color[ny][nx] == 0:
            stack = board[y][x]
            idx = stack.index(i)
            board[y][x] = stack[:idx]
            if stack[idx:]:
                board[ny][nx].extend(stack[idx:])
                if is_stop(board[ny][nx]): return True
            for num in stack[idx:]:
                horse[num] = [ny, nx, horse[num][2]]

        elif color[ny][nx] == 1:
            stack = board[y][x]
            idx = stack.index(i)
            board[y][x] = stack[:idx]
            if stack[idx:]:
                board[ny][nx].extend(stack[idx:][::-1])
                if is_stop(board[ny][nx]): return True
            for num in stack[idx:]:
                horse[num] = [ny, nx, horse[num][2]]

    # for hors in horse:
    #     print(hors)
    # print()
    # for boar in board:
    #     print(boar)
    return False


N,K = map(int,input().split())
color = [list(map(int,input().split())) for _ in range(N)]
horse = [[]] #[y,x,dir]

moves = [[-1,-1],[0,1],[0,-1],[-1,0],[1,0]]
board = [[[] for _ in range(N)] for _ in range(N)]
opposite_dict = {1:2,2:1,3:4,4:3}
for i in range(1,K+1):
    y,x,dir = map(int,input().split())
    board[y-1][x-1].append(i)
    horse.append([y-1,x-1,dir])
# print(board)
# for hors in horse:
#     print(hors)
# print()

for ans in range(1,1000+1):
    if turn1():
        print(ans)
        break
    # print('next')
else:
    print(-1)


