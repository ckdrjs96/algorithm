def subtree(now):
    global cnt

    if now==0:
        return

    cnt+=1

    #if문 필요없이 그냥해도된다
    if son2[now] !=0:
        now2=son2[now]
        subtree(now2)

    now=son1[now]
    subtree(now)


#T=1
T =int(input())
for test_case in range(1, T + 1):
    E,N=map(int, input().split())
    line = list(map(int, input().split()))

    heads=line[::2]
    tails=line[1::2]
    pairs=list(zip(heads,tails))

    son1=[0]*(E+2)
    son2=[0]*(E+2)

    for head,tail in pairs:
        if son1[head] == 0:
            son1[head] =tail
        else:
            son2[head]=tail

    cnt=0
    subtree(N)
    print(f'#{test_case}',cnt)


