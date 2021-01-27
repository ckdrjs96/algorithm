#quick sort

def partition(arr,l,r):
    p=arr[l]
    i=l+1
    j=r
    while i<=j:
        while (i<=j and arr[i]<=p):
            i+=1
        while (i<=j and arr[j]>=p):
            j-=1

        if i<=j: #피벗을 제외하고 서로 스왑하며 정렬
            arr[i], arr[j] = arr[j], arr[i]

    #피벗과 큰수가 스왑
    arr[l],arr[j]=arr[j],arr[l]

    #다음 피벗 위치를 반환환
    return j

def quicksort(arr,l,r):
    if l<r:
        p=partition(arr,l,r)
        quicksort(arr,l,p-1) #피벗 왼쪽부분을 가지고 정렬
        quicksort(arr,p+1,r) #피벗 오른쪽부분을 가지고 정렬

#T=1

T =int(input())
for test_case in range(1, T + 1):
    N=int(input())
    arr=list(map(int, input().split()))
    quicksort(arr,0,len(arr)-1)
    print(f'#{test_case}',arr[N//2])