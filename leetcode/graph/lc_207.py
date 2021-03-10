class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        traced = set()
        visited = set()

        def dfs(i):
            # 순환구조이면 False
            if i in traced:
                return False
            # 이미 방분한경로는 순환구조가 아닌것을 확인했음 탐색종료(가지치기)
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False
        return True
