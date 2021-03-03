def subset(i,k):

    if k > sumlist[i] or i==0 or k<0:
        return 0

    now=0
    if k==i:
        now=1
    #case1: 숫자 i를 포함안한경우
    case1=subset(i-1,k)
    #case2: 숫자 i를 포함 한경우
    case2=subset(i-1,k-i)
    cnt=case1+case2+now
    return cnt

#T=1
T =int(input())
for test_case in range(1, T + 1):
    N,K = map(int, input().split())
    sumlist=[int(i*(i+1)/2) for i in range(N+1)]
    cnt=0
    print(f'#{test_case}',subset(N,K))