## Bubble sort

def bubble_sort(length,arr):
    for i in range(length-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

#T=1
T = int(input())
for test_case in range(1, T + 1):
    length=int(input())
    arr=list(map(int,input().split()))
    arr_sort=bubble_sort(length,arr)
    print(f'#{test_case}',arr_sort[-1]-arr_sort[0])