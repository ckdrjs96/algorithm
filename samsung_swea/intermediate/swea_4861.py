def palindrome(board,N,M):
    #가로 확인
    for i in range(N):
        now = board[i]
        for idx in range(N-M+1):
            test=now[idx:idx+M]
            if test==test[::-1]:
                return test

    #세로 확인
    for i in range(N):
        now=[]
        for j in range(N):
            now.append(board[j][i])

        for idx in range(N-M+1):
            test=now[idx:idx+M]
            if test==test[::-1]:
                return test


T=1
#T =int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    board=[]
    for _ in range(N):
        a=list(input())
        board.append(a)

    ans=palindrome(board,N,M)
    print(f'#{test_case}',''.join(ans))



