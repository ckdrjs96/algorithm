







#T=1
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    i=0
    print(f'#{test_case}',end=' ')
    while arr:
        i+=1
        if i%2!=0:
            print(arr.pop(),end=' ')
        else:
            print(arr.pop(0),end=' ')
        if i==10:
            break
    print()