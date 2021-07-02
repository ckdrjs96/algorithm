import sys
input = sys.stdin.readline
n=int(input())
stack=[]
max_area=0
stack.append(int(input()))
for _ in range(n-1):
    long = int(input())
    stack.append(long)
    size = []
    for hight in range(1,long+1):
        count=1
        for j in stack[:-1][::-1]:
            if j<hight:
                break
            count+=1

        size.append(count*hight)
    max_area=max(max(size), max_area)
print(max_area)










