from collections import defaultdict


def solution(n, start, end, roads, traps):
    graph_o = defaultdict(list)
    graph_t = defaultdict(list)
    check=defaultdict(list)
    for s, e, cost in roads:
        graph_o[s].append([cost, e])
        graph_t[e].append([cost, s])
        if s in traps:
            check[s].append(e)
        if e in traps:
            check[e].append(s)

    node_o = [0, start]
    node_t = []
    dp = [0] * (n + 1)
    trap = False
    global ans
    ans = float('inf')
    visited=[0]*(n+1)
    visited_t=[]
    condition=[False]*(n+1)
    def dfs(x,tot):
        global ans
        trap=condition[x]
        print(x,tot,trap)
        if tot > ans:
            return
        if x == end:
            ans = min(tot, ans)
            return

        if trap:
            graph=graph_t
        else:
            graph=graph_o

        for cost,node in graph[x]:
            if visited[node]==3:
                continue
            visited[node] += 1
            if node in traps:
                condition[node] = not condition[node]
                for nod in check[node]:
                    # print(node,nod,'check')
                    condition[nod]=not condition[nod]
                print(condition)
                dfs(node,tot+cost)
                condition[node] = not condition[node]
                for nod in check[node]:
                    # print(node,nod,'check')
                    condition[nod]=not condition[nod]
            else:
                dfs(node,tot+cost)

    dfs(start,0)


    return ans

print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3]))

    # while node_o or node_t:
    #     if trap:
    #         cost, x = node_t.pop(0)
    #     else:
    #         cost, x = node_o.pop(0)
    #     if cnt + cost > ans:
    #         continue
    #     if x == end:
    #         ans = min(cnt + cost, ans)
    #         continue
    #
    #     # 어떤 그래프 사용할건지 설정
    #     graph = graph_o
    #     if x in traps:
    #         graph = graph_t
    #
    #     for node in graph[x]:
    #         stack.append(x)