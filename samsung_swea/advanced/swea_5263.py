#동적계획법
#T=1
T =int(input())
import math
for test_case in range(1, T + 1):
    N= int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    for k in range(N):
        for i in range(N):
            if k==i:
                continue
            for j in range(N):
                if i==j or k==j:
                    continue

                # 이동가능하지 않으면 가중치를를 무한대로 변환
                if graph[i][k]==0:
                    graph[i][k] =math.inf
                if graph[k][j] ==0:
                    graph[k][j] =math.inf
                if graph[i][j] ==0:
                    graph[i][j] =math.inf

                graph[i][j]=min(graph[i][k]+graph[k][j],graph[i][j])

    print(f'#{test_case}',max(sum(graph,[]))) #일차원리스트로 변환후 최댓값
