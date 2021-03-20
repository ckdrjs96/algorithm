#정답

N=int(input())
graph=list(map(int,list(input())))
cost=[0]*N
cost[0]=1
for idx,val in enumerate(graph):
    if idx==1 and val==1:
        cost[idx]=1
    if idx>1 and val==1:
        cost[idx]=cost[idx-1]+cost[idx-2]
print(cost[-1])



