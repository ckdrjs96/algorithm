def find2(n,maze):
    for i in range(n):
        for j in range(n):
            if maze[i][j]==2:
                return i, j

def dfs(n,maze):
    stack=[]
    stack.append(list(find2(n,maze)))
    move=[[-1,0],[1,0],[0,-1],[0,1]]

    while stack:
        #print(stack)
        i, j = stack.pop()
        for a, b in move:
            if 0 <= i + a < n and 0 <= j + b < n:
                if maze[i + a][j + b] == 0:
                    #방문하면 1로 바꿈
                    maze[i + a][j + b] =1
                    stack.append([i + a, j + b])

                elif maze[i+a][j+b]==3:
                    return 1
    return 0


#T=1
T =int(input())
for test_case in range(1, T + 1):
    maze=[]
    n=int(input())

    for _ in range(n):
        row=list(map(int,list(input())))
        maze.append(row)

    print(f'#{test_case}',dfs(n,maze))