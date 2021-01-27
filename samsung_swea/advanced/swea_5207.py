

#T=1
T =int(input())
for test_case in range(1, T + 1):
    N,M=map(int, input().split())
    A=sorted(list(map(int, input().split()))) #문제에서 정렬해서 저장하라했다
    B = list(map(int, input().split()))

    cnt=0

    for val in B:
        l = 0
        r = N - 1
        before=None
        while l <= r:
            m=(l+r)//2

            if A[m] == val:
                cnt+=1
                break

            elif A[m] > val:
                r=m-1
                state=1 #현재 왼쪽상태이다

            elif A[m] < val:
                l=m+1
                state=-1 #현재 오른쪽상태이다

            if before==state: #이천상태와 현재 상태가 같으면 아니다
                break
            before=state



    print(f'#{test_case}',cnt)