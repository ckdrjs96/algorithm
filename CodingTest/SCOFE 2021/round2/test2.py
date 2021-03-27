import collections,heapq
n=int(input())
graph=collections.defaultdict(list)
for _ in range(n):
    line=input().split()
    graph[line[0]].append([line[1],int(line[2])])
    graph[line[1]].append([line[0],int(line[2])])

print(graph)
start=list(graph.keys())[0]
dist=collections.defaultdict(int)
Q=[[0,start]]
while Q:
    cost,city=heapq.heappop(Q)
    print(cost,city)
    if city not in dist:
        dist[city]=cost
        for next_city,resource in graph[city]:
            heapq.heappush(Q,[resource,next_city])
    print(dist,Q)
print(sum(dist.values()))