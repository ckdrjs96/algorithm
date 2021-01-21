def binary_serch(p,target):
    l=1
    r=p
    cnt=0
    while True:
        cnt+=1
        c=int((l+r)/2)

        if c==target:
            break
        elif c < target:
            l=c
        else:
            r=c
        #print(c)
    return cnt



#T=1
T = int(input())
for test_case in range(1, T + 1):
    p,a,b = map(int, input().split())
    first=binary_serch(p,a)
    second=binary_serch(p,b)

    if first>second:
        ans='B'
    elif first<second:
        ans='A'
    else:
        ans=0
    print(f'#{test_case}', ans)
