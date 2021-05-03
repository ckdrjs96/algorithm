def solution(n, lost, reserve):
    #여분으로 챙긴학생이 도난 당한경우 제거
    lost = set(lost)
    reserve = set(reserve)
    inter = lost & reserve
    lost = list(lost - inter)
    reserve = list(reserve - inter)
    cnt = n - len(lost)

    lost.sort(reverse=True)
    #앞학생 무조건 먼저 빌려주기
    while lost:
        student = lost.pop()
        if student - 1 in reserve:
            reserve.remove(student - 1)
            cnt += 1
        elif student + 1 in reserve:
            reserve.remove(student + 1)
            cnt += 1
    return cnt