def solution(d, budget):
    d.sort()
    cnt=0
    while cnt<len(d):
        budget-=d[cnt]
        if budget<0:
            return cnt
        cnt+=1
    return cnt