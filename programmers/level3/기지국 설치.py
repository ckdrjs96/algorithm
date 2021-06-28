def solution(n, stations, w):
    stations=[-w]+stations+[n+w+1]
    ans = 0

    for i in range(len(stations)-1):
        #빈칸 개수세기
        blank=stations[i+1]-stations[i]-2*w-1
        if blank >0:
            ans+=(blank-1)//(2*w+1)+1
    return ans