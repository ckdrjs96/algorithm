#시간초과
#일일이 요소별로 탐색안하고 합을 이용했으면 해결했을듯

def box(size,points):
    ans_points=[]
    stop=False
    for i,j in points:
        for n in range(0,size):
            for m in range(0,size):
                if graph[i+n][j+m]==0:
                    stop=True
                    break
            if stop:
                stop=False
                break
        else:
            ans_points.append([i,j])
    # print(ans_points)
    return len(ans_points), ans_points
N=int(input())
graph=[list(map(int,list(input()))) for _ in range(N)]
print(graph)

point1=[]
ans=[]
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            point1.append([i,j])
# print(point1)
ans.append(len(point1))

for i in range(2,N+1):
    cnt,point1=box(i,point1)
    ans.append(cnt)
# print(ans)
print(f'total: {sum(ans)}')
for i in range(N):
    if ans[i]!=0:
        print(f'size[{i+1}]: {ans[i]}')