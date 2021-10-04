def ispass(blocks):
    start = 0
    same_hight = 1
    while start < len(blocks)-1:
        if blocks[start] == blocks[start+1]:
            start+=1
            same_hight +=1
        elif abs(blocks[start] - blocks[start + 1]) >1:
            return False
        elif blocks[start] - blocks[start+1] == -1:
            if same_hight >= L:
                start+=1
                same_hight = 1
            else:
                return False
        elif blocks[start] - blocks[start+1] == 1:
            if blocks[start+1:start+L+1] == [blocks[start+1]]*L:
                start+=L
                same_hight = 0
            else:
                return False
    return True



N, L = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
row = sum([ispass(line) for line in board])
#전치행렬 만들기
for i in range(N):
    for j in range(i,N):
        board[i][j],board[j][i] = board[j][i], board[i][j]
col=sum([ispass(line) for line in board])
print(row+col)