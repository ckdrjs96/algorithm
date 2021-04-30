#문제이상 테케오류 이슈, 시간초과도 없는 이슈
import heapq

def solution(operations):
    heap= []

    for operation in operations:
        # print(heap)
        com, val = operation.split()

        if com == 'I':
            heapq.heappush(heap, int(val))

        else:
            if val=='1' and heap:
                heap=list(map(lambda x:-x,heap))
                heapq.heapify(heap)
                heapq.heappop(heap)
                heap=list(map(lambda x:-x,heap))
                heapq.heapify(heap)
            elif val=='-1' and heap:
                heapq.heappop(heap)
    if heap:
        return [max(heap),min(heap)]
    else:
        return [0,0]


