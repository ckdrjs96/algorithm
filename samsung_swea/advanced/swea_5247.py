from collections import deque
#데크 사용하지 않으면 시간초과

def add(val):
    val+=1
    return val

def minus(val):
    val-=1
    return val

def multiply(val):
    val*=2
    if val > M+100:
        return -1
    return val

def minus10(val):
    val-=10
    return val

def bfs(N):
    cnt=0
    q=deque()
    q.append(N)
    # q:현재 같은 횟수 계산 값
    # q2: 현재 값을 통해 나온 값 저장
    while q:
        cnt+=1
        q2=deque()
        while q:
            now = q.pop()
            for fuc in calculate:
                test=fuc(now)
                if test==M:
                    return cnt

                #이미사용되었거나 값이 0과 백만사이 아니면 제외
                if test > 1000000 or test<0 or num_lst[test]:
                    continue

                num_lst[test]=True
                q2.append(test)
        q=q2


#T=1
T =int(input())
for test_case in range(1, T + 1):
    num_lst = [False] * 1000001
    N,M=map(int, input().split())
    calculate=[add,minus,multiply,minus10]
    print(f'#{test_case}',bfs(N))



