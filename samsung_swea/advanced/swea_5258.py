#recursion and memoization
#T=1
def knapsack(i,w):
    if K[i][w]!=-1:
        return K[i][w]
    if i==0 or w==0:
        K[i][w]=0
        return K[i][w]
    else:
        #case1: i번쨰 물체를 선택해서 이전 물체에서 가방크기를 줄여서 다시 최대 비용을 구함
        if w>=weight[i]:
            case1 = knapsack(i-1,w-weight[i])+value[i]
        else:
            case1=0
        #case2: i번쨰 물건을 선택안해서 이전 물체에서 같은 가방크기 만큼 남음
        case2 = knapsack(i-1,w)
        K[i][w]=max(case1,case2)
        return K[i][w]

T =int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    weight=[0]
    value=[0]
    for _ in range(M):
        w,v=map(int, input().split())
        weight.append(w)
        value.append(v)

    K=[[-1]*(N+1) for _ in range(M+1)]
    print(f'#{test_case}',knapsack(M,N))
