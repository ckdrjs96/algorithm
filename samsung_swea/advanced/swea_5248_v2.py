def find_set(x): #x가 들어 있는 집합의 대표자를 찾기
    if parent[x]==x:
        return x
    else:
        return find_set(parent[x])

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    parent[y]=x #y집합을 x에 합침(x의 대표자로)


T=1
#T =int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr=list(map(int, input().split()))
    parent = [i for i in range(N + 1)] #각자 자신이 대표자로 생성
    for i in range(M): #두학생을 같은 그룹으로 합치기
        union(arr[2 * i], arr[2 * i + 1])

    ans=[]
    cnt=-1 #0번이 없는데 포함되서 -1
    for i in range(N+1):
        if i==find_set(i): #자기자신이 대표자찾기(그룹개수)
            cnt+=1

    print(f'#{test_case}', cnt)
