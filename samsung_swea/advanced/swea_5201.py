#T=1
T =int(input())
for test_case in range(1, T + 1):
    N,M=map(int,input().split())
    containers=list(map(int,input().split()))
    trucks=list(map(int,input().split()))
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    ans=[]
    #무거운것 부터 먼저비교
    for container in containers:
        for truck in trucks:
            #컨테이너의 용량이 작아 이동
            if container <= truck:
                ans.append(container)
                trucks.remove(truck)
                break
    print(f'#{test_case}',sum(ans))

