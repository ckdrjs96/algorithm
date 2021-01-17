#가위바위보
def rsp(idx_a,num_a,idx_b,num_b):
    if num_a==num_b:
        return idx_a, num_a
    elif num_a==1:
        if num_b==2:
            return idx_b,num_b
        else:
            return idx_a, num_a

    elif num_a==2:
        if num_b==3:
            return idx_b,num_b
        else:
            return idx_a, num_a

    elif num_a==3:
        if num_b==1:
            return idx_b,num_b
        else:
            return idx_a, num_a

#리스트를 슬라이싱 말고 인덱스만 하면 좀더 효율적
def twogroup(n,game):
    if n==2:
        return rsp(0,game[0],1,game[1])
    elif n==1:
        return 0,game[0]

    new_n=(n+1)//2

    idx_a,num_a = twogroup(new_n,game[:new_n])
    idx_b,num_b = twogroup(n-new_n,game[new_n:])
    idx_b+=new_n #뒤쪽그룹은 앞의 개수만 큼 인덱스를 뒤로한다

    idx,num=rsp(idx_a,num_a,idx_b,num_b)

    return idx,num

T =int(input())
for test_case in range(1, T + 1):
    n = int(input())
    game = list(map(int, input().split()))
    print(f'#{test_case}',twogroup(n, game)[0]+1) #인덱스번호가 아니라 +1해준다
