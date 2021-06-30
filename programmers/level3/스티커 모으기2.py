def solution(sticker):
    n=len(sticker)

    def collect(start):
        dp=[0]*n
        dp[start]=sticker[start]
        dp[start+1]=sticker[start]
        for i in range(start+2,n-1+start):
            dp[i%n] = max(dp[(i-1)%n],dp[(i-2)%n]+sticker[i%n])
        return dp[(start-2+n)%n]

    if n<4:
        return max(sticker)
    return max(collect(0),collect(1),collect(2)) #시작점 위치 0,1,2