#정답
prefer=list(map(float,input().split()))
N,M=list(map(int,input().split()))
watch=[list(input()) for _ in range(N)]
genre=[list(input()) for _ in range(N)]
prefer_map={'A':prefer[0],'B':prefer[1],'C':prefer[2],'D':prefer[3],'E':prefer[4]}

find_y=[]
find_o=[]
for i in range(N):
    for j in range(M):
        if watch[i][j]=='Y':
            find_y.append([i,j])
        elif watch[i][j]=='O':
            find_o.append([i,j])
find_y=sorted(find_y,key=lambda x:prefer_map[genre[x[0]][x[1]]],reverse=True)
find_o.sort(key=lambda x:prefer_map[genre[x[0]][x[1]]],reverse=True)
# find_y.sort(key=lambda x:prefer_map[genre[i][j]])
# print(find_y)
# print(find_o)
for n,m in find_y:
    genreee=genre[n][m]
    print(f'{genreee} {prefer_map[genreee]} {n} {m}')
for n,m in find_o:
    genreee=genre[n][m]
    print(f'{genreee} {prefer_map[genreee]} {n} {m}')