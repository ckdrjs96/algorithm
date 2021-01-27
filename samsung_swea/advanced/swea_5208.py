def go(arr,busstop,battary):
    global cnt,ans
    #가지치기
    if cnt > ans:
        return

    #N보다 크면거나 같으면 도착
    if busstop+battary >=N:
        ans=min(ans,cnt) #가능한 교환횟수중 작은값 저장
        return

    for i in range(battary,0,-1):
        cnt+=1
        go(arr,busstop+i,arr[busstop+i])
        cnt-=1



#T=1
T =int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    N=arr[0]
    cnt=0
    ans=10000  #가능한 최대값
    go(arr,1,arr[1])
    print(f'#{test_case}',ans)