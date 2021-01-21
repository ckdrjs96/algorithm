### use list

def sum_list(sumlist, new):
    for idx, data in enumerate(sumlist):
        if data > new[0]:
            sumlist[idx:idx] = new
            #sumlist = sumlist[:idx] + new + sumlist[idx:]
            #느리다
            break
    else:
        sumlist = sumlist + new

    return sumlist

T = int(input())
for test_case in range(1, T + 1):
    N,M=map(int,input().split())
    sumlist=[]
    for _ in range(M):
        new=list(map(int,input().split()))
        if sumlist:
            sumlist=sum_list(sumlist,new)
        else:
            sumlist=new

    print(f'#{test_case}',end=' ')
    print(*sumlist[len(sumlist)-10:][::-1])
