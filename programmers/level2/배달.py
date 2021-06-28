from collections import defaultdict
import heapq

def solution(N, road, K):
    if N==1:
        return 1

    graph = defaultdict(list)
    for s,e,cost in road:
        graph[s].append([e,cost])
        graph[e].append([s,cost])

    move=[float('inf')]*(N+1)
    #VISITED 방문했어도 작은 경로로 다시 올수있음 따라서 필요없다
    q=[[0,1]]
    move[1]=0
    while q:
        time, node=heapq.heappop(q)

        for e,cost in graph[node]:
            #더 오래걸린는 경로가 주어지면 무시시
            if min(move[e],move[node]+cost) ==move[e]:
                continue
            q.append([min(move[e],move[node]+cost),e])
            move[e]=min(move[e],move[node]+cost)
        # print(move)

    return len(list(filter(lambda x:x<=K,move)))