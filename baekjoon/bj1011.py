import sys
input=sys.stdin.readline
a,b=map(int,input().split())
sieve=[True]*(b+1)
for j in range(2,int(b**0.5)+1):
    if sieve[j]==True:
        for i in range (j+j,b+1,j):
            sieve[i]=False
print(sieve)
for i in range(2,b+1):
    if sieve[i]==True: sieve[i]=i
print(sieve)
for i in range(2,len(sieve)):
    if sieve[i]>=a: print(sieve[i])
