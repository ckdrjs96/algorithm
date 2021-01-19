#혼자해결못함 아래의 도움
#https://hongsj36.github.io/2020/01/23/IM_Stack2/

def check(row,visited):

    global all_sum, min_sum

    #가지치기
    #이미 최소값을 넘었으면
    if all_sum > min_sum:
        return

    #마지막줄이면 최솟값비교
    if row == n:
        min_sum=min(all_sum,min_sum)
        return

    for col in range(n):
        if not visited[col]:
            visited[col]=True
            all_sum+=board[row][col]
            check(row+1,visited)

            visited[col]=False
            all_sum-=board[row][col]



#T=1
T =int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board=[]
    for _ in range(n):
        line=list(map(int,input().split()))
        board.append(line)

    all_sum=0
    min_sum=1000
    visited=[False]*n
    check(0, visited)
    print(f'#{test_case}',min_sum)
