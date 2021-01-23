def move(i,j):
    global ans,ans_min
    #가지치기
    if ans > ans_min:
        return
    #범위 넘어가면 종료
    if i>=N or j>=N:
        return

    ans+=board[i][j]
    #최종지점 토착하면 계산
    if i==N-1 and j==N-1:
        ans_min=min(ans,ans_min)
    #오른쪽이동
    move(i+1,j)
    #왼쪽이동
    move(i,j+1)
    #값 원상복구
    ans -= board[i][j]





#T=1
T =int(input())
for test_case in range(1, T + 1):
    N=int(input())
    board=[list(map(int,input().split())) for _ in range(N)]
    ans=0
    ans_min=250 #최대 가능한 것이 250
    move(0,0)
    print(f'#{test_case}',ans_min)
