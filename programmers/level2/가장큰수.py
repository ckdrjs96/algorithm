#분할정복
def solution(numbers):
    numbers = list(map(str, numbers))

    def di_qu(numbers):
        n = len(numbers)
        if n == 1:
            return numbers

        lefts = di_qu(numbers[:n // 2])
        rights = di_qu(numbers[n // 2:])

        next = []
        while lefts and rights:
            if lefts[0] + rights[0] > rights[0] + lefts[0]:
                next.append(rights.pop(0))
            else:
                next.append(lefts.pop(0))

        if lefts:
            next += lefts
        if rights:
            next += rights
        return next

    return str(int(''.join(di_qu(numbers)[::-1])))






#블로그 참조
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x[0], x[1 % len(x)], x[2 % len(x)], x[3 % len(x)]), reverse=True)
    return str(int("".join(numbers)))

###다른풀이

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer