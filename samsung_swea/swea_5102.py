def make_map(e):
    mapping = dict()
    for _ in range(e):
        first, second = map(int, input().split())
        if first in mapping:
            mapping[first].append(second)
        else:
            mapping[first] = [second]

        if second in mapping:
            mapping[second].append(first)
        else:
            mapping[second] = [first]

    return mapping


def runs(mapping):
    start, second = map(int, input().split())

    if start == second:
        return 0

    queue = [start]
    i = 1
    visited = [start]

    while queue:

        queue2 = []
        while queue:
            now = queue.pop()

            for k in mapping[now]:
                if k == second:
                    return i

                elif k not in visited:
                    visited.append(k)
                    queue2.append(k)

        queue = queue2

        i += 1

    return 0


T = int(input())

for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    mapping = make_map(e)
    print(f'#{test_case} {runs(mapping)}')