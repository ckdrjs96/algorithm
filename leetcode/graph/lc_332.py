class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        cities = sorted(list(set(sum(tickets, []))))

        graph = [[0] * len(cities) for _ in range(len(cities))]
        #사전순으로 그래프 민들기
        for city_from, city_to in tickets:
            graph[cities.index(city_from)][cities.index(city_to)] += 1
        start = cities.index('JFK')

        ans2 = []

        def dfs(start):

            for idx, val in enumerate(graph[start]):
                if val > 0:
                    graph[start][idx] -= 1
                    dfs(idx)
            ans2.append(cities[start])

        dfs(start)
        return ans2[::-1]