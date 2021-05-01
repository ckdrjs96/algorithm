def solution(citations):
    n=len(citations)
    for i in range(n,-1,-1):
        cite=len(list(filter(lambda x:x>=i, citations)))
        if cite >=i:
            return i
    answer = 0
    return answer