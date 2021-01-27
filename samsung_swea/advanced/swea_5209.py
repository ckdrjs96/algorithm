def money(row):
    global sums,ans

    #끝 행까지 도착하면 최소답과 비교
    if row==N:
        ans=min(sums,ans)
        return
    #가지치기
    if sums>ans:
        return

    for i in range(N):
        if visit_col[i]==False:
            visit_col[i]=True
            sums+=matrix[row][i]
            money(row+1)

            #되돌아가기
            visit_col[i]=False
            sums-=matrix[row][i]

#T=1
T =int(input())
for test_case in range(1, T + 1):
    N=int(input())
    matrix=[list(map(int, input().split())) for _ in range(N)]
    sums=0
    ans=1500 #가능한 최대값
    visit_col=[False]*N
    money(0)
    print(f'#{test_case}',ans)