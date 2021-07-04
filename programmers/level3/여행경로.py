from collections import defaultdict
def solution(tickets):
    graph = defaultdict(list)
    for start,end in sorted(tickets,reverse=True):
        graph[start].append(end)
    ans=[]

    def dfs(x):
        while graph[x]:
            dfs(graph[x].pop())
        #더이상 없으면 정답에 추가(뒤쪽 부터 해결되므로 역순으로 추가됨)
        ans.append(x)

    dfs('ICN')
    return ans[::-1]