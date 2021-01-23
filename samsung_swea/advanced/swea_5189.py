#계산하기
def move(arr):
    global ans_min
    arr=[1]+arr+[1]
    ans=0
    for i in range(len(arr)-1):
        ans+=board[arr[i]-1][arr[i+1]-1]
    if ans_min==None:
        ans_min=ans
    else:
        ans_min=min(ans_min,ans)

#방문할 구역 순서정하기
def swap(i):
    #순서정해졌으면 값계산
    if i==N-2:
        move(arr)

    for j in range(i,N-1):
        arr[i],arr[j]=arr[j],arr[i]
        swap(i+1)
        arr[i], arr[j] = arr[j], arr[i]



#T=1
T =int(input())
for test_case in range(1, T + 1):
    N=int(input())
    board=[list(map(int,input().split())) for _ in range(N)]
    arr=[i for i in range(2,N+1)]
    ans_min=None
    swap(0)
    print(f'#{test_case}',ans_min)