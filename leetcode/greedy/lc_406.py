class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 최대 힙으로 우선순위큐에 저장
        for person in people:
            heapq.heappush(heap, [-person[0], person[1]])
        ans = []
        # 해당 인댁스에 삽입
        while heap:
            h, k = heapq.heappop(heap)
            ans.insert(k, [-h, k])

        return ans