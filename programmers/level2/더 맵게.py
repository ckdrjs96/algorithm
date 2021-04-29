import heapq
def solution(scoville, K):
    ans = 0
    heapq.heapify(scoville)
    while (scoville):
        first=heapq.heappop(scoville)
        if first>=K:
            return ans
        if scoville:
            second=heapq.heappop(scoville)
        else:
            return -1
        heapq.heappush(scoville,first+second*2)
        ans+=1

    return ans