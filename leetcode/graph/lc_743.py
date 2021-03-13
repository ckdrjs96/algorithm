class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1~n 을 0~n-1로
        # graph 만들기
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u - 1].append([v - 1, w])

        inf = float('inf')
        def dijkstra():

            D = [inf] * n
            visited = [False] * n
            D[k - 1] = 0

            # 0~n-1의 정점을 모두 탐색한다
            for _ in range(n):
                min = inf
                minidx = -1
                for i in range(n):
                    if not visited[i] and D[i] < min:
                        min = D[i]
                        minidx = i
                visited[minidx] = True

                for to, val in graph[minidx]:
                    if not visited[to] and D[to] > D[minidx] + val:
                        D[to] = D[minidx] + val
                # print(D)
            return D

        D = dijkstra()

        if max(D) == inf:
            ans = -1
        else:
            ans = max(D)
        return ans