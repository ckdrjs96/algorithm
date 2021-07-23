import sys
N=int(input())
t_cost=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
time = [0] *(N+2)
for i in range(1,N+1):
    t,p=t_cost[i-1]
    if i+t<=N+1:
        for idx in range(i+t,N+2):
            time[idx] = max(time[i]+p,time[idx])
    # print(time)
print(time[-1])

#뒤에서 부터 dp하는 것이 더 효율적