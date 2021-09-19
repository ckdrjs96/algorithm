#벽세우는데 어려움
#deque 사용하면 1208ms 로 증가?? pop(0)는 1060ms
import sys
from copy import deepcopy
from collections import deque

def find_birus(graph):
    birus_list = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                birus_list.append([i,j])
    return birus_list

def safe_count(graph):
    n = len(graph)
    m = len(graph[0])
    birus_list = find_birus(graph)
    moves = [[1,0],[0,1],[-1,0],[0,-1]]


    for birus_y,birus_x in birus_list:
        q = deque()
        q.append([birus_y,birus_x])
        # q = [[birus_y,birus_x]]
        graph[birus_y][birus_x] = 1
        while q:
            # y,x = q.pop(0)
            y,x = q.popleft()
            for dy,dx in moves:
                if 0<=y+dy<n and 0<=x+dx<m and graph[y+dy][x+dx] == 0:
                    graph[y + dy][x + dx] = 1
                    q.append([y+dy,x+dx])
    return graph


def select_wall(start, count):
    global max_value
    if count == 3:  # 종료조건, 벽 3개 선택 완료
        graph = safe_count(deepcopy(board))  # deepcopy로 벽이 선택된 배열 복사
        safe_counts = sum(ilne.count(0) for ilne in graph)  # clean 지역 count
        max_value = max(max_value, safe_counts)

    else:
        for i in range(start, N * M):  # 2차원 배열에서 조합 구하기
            r = i // M
            c = i % M
            if board[r][c] == 0:  # 안전영역인 경우 벽으로 선택가능
                board[r][c] = 1  # 벽으로 변경
                select_wall(i, count + 1)  # 벽선택
                board[r][c] = 0




N,M =map(int,input().split())
input = sys.stdin.readline
board = [list(map(int,input().split())) for _ in range(N)]

max_value = 0
select_wall(0,0)
print(max_value)

