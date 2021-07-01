def solution(dirs):
    global ans
    ans = 0
    def check(r_c,x,y):
        global ans
        if not visitied[r_c][y][x]:

            ans+=1
            # print(r_c,x,y,ans)
            visitied[r_c][y][x]=True
        return
    #[가로,세로]
    visitied = [[[False]*11 for _ in range(11)],[[False]*11 for _ in range(11)]]
    #(5,5) -> 실제 (0,0)

    x=y=5
    for com in dirs:
        if com == 'U':
            if y <10:
                check(1,x,y)
                y+=1
        elif com == 'D':
            if y >0:
                y-=1
                check(1,x,y)
        elif com == 'R':
            if x<10:
                check(0,x,y)
                x+=1
        elif com == 'L':
            if x>0:
                x-=1
                check(0,x,y)
        # print(x,y)
    return ans

##다른 풀이
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2