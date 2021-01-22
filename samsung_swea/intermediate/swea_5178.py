

#T=1
T =int(input())
for test_case in range(1, T + 1):
    N,M,L=map(int,input().split())
    tree=[0]*(N+1)
    #리프노드값 저장
    for _ in range(M):
        node,val = map(int, input().split())
        tree[node]=val

    #뒤에 노드부터 루트 노드에 더해주기
    for i in range(N,1,-1):
        tree[i//2]+=tree[i]

    print(f'#{test_case}',tree[L])