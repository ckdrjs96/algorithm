from collections import defaultdict
import heapq


def solution(n, costs):
    graph = defaultdict(list)
    for start, finish, cost in costs:
        graph[start].append([cost, finish])
        graph[finish].append([cost, start])
    #0부터 시작
    heap = [[0, 0]]
    cnt = 0
    #방문확인
    visited = [False] * n

    while heap:
        cost, next = heapq.heappop(heap)
        if not visited[next]:
            visited[next] = True
            for cos, nex in graph[next]:
                if not visited[nex]:
                    heapq.heappush(heap, [cos, nex])
            cnt += cost

    return cnt