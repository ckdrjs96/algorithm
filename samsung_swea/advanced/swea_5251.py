def dijkstra(G):
    inf=float('inf')
    D=[inf]*(N+1)
    p=[None]*(N+1) #최단경로트리
    visitied=[False]*(N+1)
    D[0]=0

    for _ in range(N):
        minindex=-1
        min=inf
        for i in range(N):
            if not visitied[i] and D[i]<min:
                minindex=i
                min=D[i]
        visitied[minindex]=True

        for v,val in G[minindex]:
            if not visitied[v] and D[minindex]+val < D[v]:
                D[v]=D[minindex]+val
                p[v]=minindex


    return D[-1]

#T=1
T =int(input())
for test_case in range(1, T + 1):
    N,E= map(int, input().split())
    #board=[list(map(int, input().split())) for _ in range(E)]
    graph=dict()
    for _ in range(E):
        s,e,w=map(int, input().split())
        if s in graph:
            graph[s].append([e,w])
        else:
            graph[s]=[[e,w]]
    print(f'#{test_case}',dijkstra(graph))
