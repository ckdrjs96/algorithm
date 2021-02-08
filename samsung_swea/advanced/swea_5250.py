def dijkstra():
    inf=float('inf')
    drow=[0,0,1,-1]
    dcol=[-1,1,0,0]

    D=[[inf]*N for _ in range(N)] #출발점에서 각 정점까지 최단경로 를 저장
    D[0][0]=0
    q=[]
    q.append([0,0]) #시작위치
    while q:
        row,col=q.pop(0)
        for i in range(4):
            new_row=row+drow[i]
            new_col=col+dcol[i]
            if 0<=new_row<N and 0<=new_col<N:
                #높이가 높아지면 추가연료 계산 낮거나 같으면 0이다
                add_fuel = max(0, board[new_row][new_col] - board[row][col])

                #다익스트라 알고리즘
                if D[new_row][new_col] > D[row][col] + add_fuel+1:
                    D[new_row][new_col] = D[row][col] + add_fuel + 1
                    q.append([new_row,new_col])

    return D[N-1][N-1]




#T=1
T =int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board=[list(map(int, input().split())) for _ in range(N)]


    print(f'#{test_case}',dijkstra())