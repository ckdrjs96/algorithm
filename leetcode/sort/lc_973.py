class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for idx,val in enumerate(points):
            dist.append([val[0]**2+val[1]**2,idx])
        dist.sort(key=lambda x:x[0])
        idx=list(map(lambda x: x[1],dist[:k]))
        # print(idx)
        ans=[]
        for i in idx:
            ans.append(points[i])
        return ans

        #책 우선순위 큐 풀이
        # heap = []
        # for x, y in points:
        #     dist = x ** 2 + y ** 2
        #     heapq.heappush(heap, (dist, x, y))
        #
        # result = []
        # for _ in range(k):
        #     dist, x, y = heapq.heappop(heap)
        #     result.append([x, y])
        #
        # return result
