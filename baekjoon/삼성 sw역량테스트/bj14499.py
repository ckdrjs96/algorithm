import sys

def move(y,x,num):
    cant=False
    if num == 1:
        if x >M-2:
            cant =True
        else:
            x+=1
    elif num == 2:
        if x < 1:
            cant =True
        else:
            x-=1
    elif num == 3:
        if y <1:
            cant =True
        else: y-=1
    elif num ==4 :
        if y > N-2:
            cant =True
        else: y+=1
    return y,x,cant


def case_chage(num,case):
    if num ==3:
        new_case = {'now': case[3], 1:case[1],2:case[2],3:case['opposite'],4:case['now'] ,'opposite':case[4]}
    elif num ==4:
        new_case = {'now': case[4], 1: case[1], 2: case[2], 3: case['now'], 4: case['opposite'], 'opposite': case[3]}
    elif num ==1:
        new_case = {'now': case[1], 1: case['opposite'], 2: case['now'], 3: case[3], 4: case[4], 'opposite': case[2]}
    elif num ==2:
        new_case = {'now': case[2], 1: case['now'], 2: case['opposite'], 3: case[3], 4: case[4], 'opposite': case[1]}
    return new_case


N,M,y,x,K =map(int,input().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
moves = list(map(int, input().split()))
dice = [0] *6
case = {'now': 0, 1:2,2:5,3:4,4:1 ,'opposite':3}
for num in moves:
    y,x,cant = move(y,x,num)
    if cant:
        continue
    # print(y,x)
    case = case_chage(num,case)
    # print(case)
    if board[y][x] ==0:
        board[y][x] = dice[case['now']]

    else:
        dice[case['now']] = board[y][x]
        board[y][x] = 0

    print(dice[case['opposite']])
    # print(board)
    # print(dice)
    # print()




