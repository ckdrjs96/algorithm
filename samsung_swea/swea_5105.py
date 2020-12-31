def find_two(maze):
    n=len(maze)
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i,j

def bfs(maze):
    queue=[]
    queue.append(list(find_two(maze)))
    size=len(maze)
    cnt=0
    while queue:
        depth_queue=[]#각 깊이마다 큐를 처리하여 깊이를 계산한다.
        while queue:   
            m,n=queue.pop(0)#각 깊이마다 하는 반복문이라 pop()도 상관없
            for a,b in direc:
                if m+a>=0 and m+a<size and n+b>=0 and n+b<size:
                    if maze[m+a][n+b]==0:
                    	maze[m+a][n+b]=1 #지나온곳은 1로변경하여 다시 탐색하지 않도록
                    	depth_queue.append([m+a,n+b])
                    if maze[m+a][n+b]==3:
                        print(f'#{test_case} {cnt}')
                        return
        queue=depth_queue
        cnt+=1
    print(f'#{test_case} 0')    
    


T = int(input())
direc=[[1,0],[-1,0],[0,-1],[0,1]]
for test_case in range(1, T + 1):
    maze=[]


    for i in range(int(input())):
        a=list(map(int,list(input())))
        maze.append(a)
    bfs(maze)
