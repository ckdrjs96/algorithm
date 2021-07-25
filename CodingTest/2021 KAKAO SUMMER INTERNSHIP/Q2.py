def near(place):
    stack=[]
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P':
                stack.append([i,j])
    print(stack)

    moves=[[1,0],[-1,0],[0,1],[0,-1]]
    global ans
    ans=False
    def dfs(x,y,place,cnt):
        global ans
        if cnt >=2:
            return
        print(x,y,cnt)
        for m, n in moves:
            if x + m < 0 or x + m >= 5 or y + n < 0 or y + n >= 5 or place[x + m][y+n]=='X':
                continue

            if place[x + m][y + n]=='P':
                print(x + m,y + n,'wrong')
                ans=True
                return ans
            place[x + m][y + n]='X'
            dfs(x+m,y+n,place,cnt+1)
            place[x + m][y + n] = 'O'
        return ans


    while stack:
        x,y=stack.pop()
        print(x,y,'start')
        place[x][y]='X'
        if dfs(x,y,place,0):
            return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        place=[list(plac) for plac in place]
        answer.append(near(place))

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))