def heap_min(idx,val):
    #일단 삽입한다
    tree[idx]=val

    while idx>1:
        root=idx//2
        #루트노드보다 크면 스왑한다
        if tree[root] > tree[idx]:
            tree[root],tree[idx]=tree[idx],tree[root]
        #루트노드값과 바뀌지않으면 뒤는 더이상 볼필요없다
        else:
            break
        idx=root


#T=1
T =int(input())
for test_case in range(1, T + 1):
    N=int(input())
    arr=list(map(int,input().split()))

    tree=[None]*(N+1)
    for idx, val in enumerate(arr):
        idx+=1
        heap_min(idx,val)

    ans=0
    while N>1:
        N=N//2
        ans+=tree[N]

    print(f'#{test_case}',ans)
