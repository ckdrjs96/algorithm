def make_bcmap(x,y,c,p,num):
    for i in range(-c,c+1):
        for j in range(-c+abs(i),c+1-abs(i)):
            if 0<y+i<11 and 0<x+j<11:
                board[y+i][x+j].append(num)

    return board
#
def main():
    moves=[[0,0],[-1,0],[0,1],[1,0],[0,-1]]
    ay,ax,by,bx = 1,1,10,10
    max_charge = 0
    for i in range(M+1):
        # print(ay,ax,by,bx)
        if board[ay][ax] and board[by][bx]:
            # print(board[ay][ax], board[by][bx])
            max_check = 0
            for bc_a in board[ay][ax]:
                for bc_b in board[by][bx]:
                    if bc_a == bc_b:
                        check = p_dict[bc_a]
                    else:
                        check = p_dict[bc_a] + p_dict[bc_b]
                    max_check = max(max_check, check)
            # print(max_check)
            max_charge += max_check

        elif board[ay][ax]:
            charge_list = [p_dict[bc_a]  for bc_a in board[ay][ax]]
            max_charge+= max(charge_list)
        elif board[by][bx]:
            charge_list = [p_dict[bc_b] for bc_b in board[by][bx]]
            max_charge+=max(charge_list)

        if i <M:
            dy,dx = moves[user_a[i]]
            ay +=dy
            ax +=dx
            dy,dx = moves[user_b[i]]
            by +=dy
            bx +=dx

    return max_charge


T = int(input())
# T=1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    M,A = map(int,input().split())
    user_a = list(map(int,input().split()))
    user_b = list(map(int,input().split()))
    bc = [list(map(int,input().split())) for i in range(A)]

    board = [[[] for _ in range(11) ] for _ in range(11)]
    p_dict = dict()
    for num,bc_val in enumerate(bc):
        p_dict[num] = bc_val[3]
        make_bcmap(*bc_val,num)

    # for boar in board:
    #     print(boar)
    ans = main()
    print(f'#{test_case} {ans}')



