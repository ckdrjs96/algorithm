import heapq
def solution(jobs):
    n=len(jobs)
    heapq.heapify(jobs)
    cnt=tot_time=0
    while jobs:
        start,time=heapq.heappop(jobs)
        cnt+=time
        #시작이 항상 0이 아닐때를 위해서
        if tot_time==0:
            tot_time=start
        tot_time+=time
        while jobs:
            start1, time1 = heapq.heappop(jobs)
            #종료시점전에 시작하는것이 있으면 기다리는 시간을 더해주고 시점을 뒤로민다
            if start1 < tot_time:
                heapq.heappush(jobs,[tot_time,time1])
                cnt+=tot_time-start1
            else:
                heapq.heappush(jobs,[start1,time1])
                break

    return cnt//n