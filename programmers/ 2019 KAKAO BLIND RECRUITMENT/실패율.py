from collections import Counter

def solution(N, stages):
    stages_cnt = Counter(stages)
    fail_rate = [0] * N
    remain = len(stages)
    for i in range(N):
        if remain > 0:
            fail_rate[i] = [i + 1, stages_cnt[i + 1] / remain]
        else:
            fail_rate[i] = [i + 1, 0]

        remain -= stages_cnt[i + 1]
    fail_rate = sorted(fail_rate, key=lambda x: x[1], reverse=True)
    idx, _ = zip(*fail_rate)
    return idx