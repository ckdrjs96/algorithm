def make_map(E):
    mapping=dict()
    for _ in range(E):
        a,b=map(int,input().split())
        if a in mapping:
            mapping[a].append(b)
        else:
            mapping[a]=[b]
    return mapping
        
def bfs(mapping,test1,test2):
    stack=[]
    stack=mapping[test1]
    while stack:
        now=stack.pop()
        if now in mapping:
            if test2 in mapping[now]:
                return 1
            else:
                stack=stack+mapping[now]
            stack=stack+mapping[now]
        else:
            pass
    return 0


T = int(input())
for test_case in range(1, T + 1):
    V,E=map(int,input().split())
    mapping=make_map(E)
    test1,test2=map(int,input().split())
    print(f'#{test_case} {bfs(mapping,test1,test2)}')
