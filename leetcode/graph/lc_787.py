class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])

        inf = float('inf')
        D = [inf] * n
        visited = [False] * n
        D[src] = 0
        global ans
        ans = inf

        def dijkstra(time, D):
            global ans
            if time == K + 1:
                # print(D)

                return
            nextnode = []
            for i in range(n):
                if not visited[i] and D[i] != inf:
                    nextnode.append([i, D[i]])
                    # print(time,i)

                nextnode = sorted(nextnode, key=lambda x: x[1])
                for j, _ in nextnode:
                    visited[j] = True
                    after = D[:]
                    for to, val in graph[j]:
                        if not visited[to] and D[to] > val + D[j]:
                            D[to] = val + D[j]
                            if to == dst:
                                ans = min(D[dst], ans)
                                return

                    dijkstra(time + 1, D)
                    visited[i] = False
                    D = after[:]

        dijkstra(0, D)
        # print('ans',ans)
        if ans == inf:
            return -1
        else:
            return ans
