def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    n = len(food_times)
    # 위치 표시하기
    food_times = list(zip(food_times, range(1, n + 1)))
    food_times.sort(key=lambda x: x[0])

    #차이만큼 한꺼번에 뺴주기
    before = 0
    for i in range(n):
        now, idx = food_times[i]
        if k >= (now - before) * (n - i):
            k -= (now - before) * (n - i)
            before = now
        else:
            break

    #위치대로 돌려주기
    final = food_times[i:]
    final = sorted(final, key=lambda x: x[1])

    return final[k % (n - i)][1]