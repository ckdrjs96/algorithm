def solution(number, k):
    n=len(number)
    start=0
    for _ in range(k):
        for i in range(start,len(number)-1):
            if number[i] <number[i+1]:
                number=number[:i]+number[i+1:]
                start=max(i-1,0)
                break

    return number[:n-k]

#최적화로 시간초과 겨우 통과
#스택으로 풀면 더 빠르다