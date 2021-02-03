#kruskal algorithm
def find_set(x): #x가 들어 있는 집합의 대표자를 찾기
    if parent[x]==x:
        return x
    else: return find_set(parent[x])

def union(x,y):
    x=find_set(x)
    y=find_set(y)
    parent[y]=x #y집합을 x에 합침(x의 대표자로)

def mst_kruskal(G):
    mst=[]
    mst_cost=0
    while len(mst) <V: #간선이 V개 일떄까지
        u,v,val=G.pop(0) #작은순서부터
        if find_set(u) != find_set(v): #다른 그룹일떄만
            union(u,v) #두그룹 합치기
            mst_cost+=val #최소 가중치 더하기
            mst.append((u,v)) #이동간선 기록

    return mst_cost


T =int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split()) #노드개수:V+1,간선개수:E
    #그래프 저장
    G=[tuple(map(int, input().split())) for _ in range(E)]
    G.sort(key=lambda x: x[2]) #가중치 기준 정렬
    parent = [i for i in range(V + 1)] #각자 자신이 대표자로 그룹 생성
    ans=mst_kruskal(G)
    print(f'#{test_case}',ans)