N,exer_time = input().split()
times=[input() for _ in range(int(N))]
exer_time=list(map(int,exer_time.split(':')))
exer_time=exer_time[0]*3600+exer_time[1]*60+exer_time[2]
print(exer_time)
times=[list(map(int,time.split(':'))) for time in times]
times=[time[0]*60+time[1] for time in times]
print(times)

add=0
cnt=0
ans_cnt=1
ans_idx=0
for i in range(len(times)):
    if sum(times[i:i+ans_cnt-1]) >= exer_time:
        continue
    for j in range(i+ans_cnt-1,len(times)):
        if sum(times[i:j])>=exer_time:
            # print(i,j)
            if (j-i) >ans_cnt:
                ans_idx = i+1
                ans_cnt = (j-i)
            break
print(ans_cnt,ans_idx)
