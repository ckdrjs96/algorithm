def draw(arr):
    for i in range(arr[0],arr[2]+1):
        for j in range(arr[1],arr[3]+1):

            #문제에 '같은 색인 영역은 겹치지 않는다' 이므로 다음과 같아도 무방
            board[i][j]+=arr[4]
    return board

#T=1
T = int(input())
for test_case in range(1, T + 1):
    n=int(input())
    board=[[0]*10 for _ in range(10)]
    #[[0]*10]*10은 같은주소복사라 하면 안됨

    for _ in range(n):
         board=draw(list(map(int,input().split())))

    ans=0
    for i in range(10):
        ans+=board[i].count(3)
    print(f'#{test_case}',ans)