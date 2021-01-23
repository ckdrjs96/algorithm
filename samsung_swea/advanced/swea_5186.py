
#T=1
T =int(input())
for test_case in range(1, T + 1):
    N=float(input())
    now=1
    str=''
    while N>0:
        two=2**(-1*now)
        if N>=two:
            N-=two
            str+='1'
        else:
            str+='0'
        now+=1
        if now>13:
            break

    if len(str)<13:
        print(f'#{test_case}',str)
    else:
        print(f'#{test_case} overflow')