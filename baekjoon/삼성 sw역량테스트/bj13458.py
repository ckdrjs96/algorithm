N = int(input())
participants = list(map(int,input().split()))
main,sub = map(int, input().split())
for i,val in enumerate(participants):
    if val-main>=0:
        participants[i]=(val-main-1)//sub+1
    else:
        participants[i]=0
print(N+sum(participants))