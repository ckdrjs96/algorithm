#prim algorithm

def mst_prim(g,s):
    key=[math.inf]*(V+1)
    pi=[None]*(V+1)
    visited=[False]*(V+1)
    key[s]=0
    ans=0
    for _ in range(V+1): #정점 개수 만큼 반복
        minidx=-1 #초기화
        min=math.inf #초기화
        for i in range(V+1): #정점들중 최소 가중치인 정점 찾기
            if not visited[i] and key[i]<min: #방문한적없고 현재 최솟값보다 작으면
                min=key[i] #최소 가중치와
                minidx=i #최소 인덱스로 저장

        visited[minidx]=True #방문기록
        for v,val in g[minidx]: #최소 인덱스와 인접한 정점들에 대해서
            if not visited[v] and val < key[v]: #방문한적이 없고 현재 키값보다 작으면
                key[v]=val #키값
                pi[v]=minidx #트리의 부모를 기록

        ans+=min #최소가중치값 더하기
    return ans


import math
T=1
#T =int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    g=dict()
    for _ in range(E):
        first,second,val=map(int, input().split())
        #무향그래프 양방향으로 저장하기
        if first in g:
            g[first].append([second,val])
        else:
            g[first]=[[second,val]]

        if second in g:
            g[second].append([first, val])
        else:
            g[second] = [[first, val]]

    ans=mst_prim(g,0)
    print(f'#{test_case}',ans)
