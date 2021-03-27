import re
import sys
input=sys.stdin.readline
N=int(input().rstrip())
indexs=[input().rstrip() for _ in range(N)]
Q=int(input().rstrip())
searches=[input().rstrip() for _ in range(Q)]
print(searches)
for search in searches:
    cnt=0
    for index in indexs:
        if search in index:
            cnt+=1
    print(cnt)