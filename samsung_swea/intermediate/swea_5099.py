class circuleque:
    def __init__(self, k):
        self.front = 0
        self.rear = 0
        self.k = k + 1
        self.items = [None] * (self.k)

    def enQuque(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.k
            self.items[self.rear] = item

    def deQueue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.k
            return self.items[self.front]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.k

    def check(self):
        print(self.items)


def runf(N, b):
    a = circuleque(N)
    i = -1
    c = dict()
    for k in range(N):
        c[k] = 0

    j = 1
    while True:
        i = (i + 1) % N
        if not a.isFull():
            if b:
                d = b.pop(0)
                a.enQuque(d)
                c[i] = j
                j += 1

        else:
            now = a.deQueue()
            now = now // 2
            if now >= 1:
                a.enQuque(now)

            elif now == 0 and b:
                d = b.pop(0)
                a.enQuque(d)
                c[i] = j
                j += 1

            else:
                a.enQuque(0)
                if i in c:
                    del c[i]

                if len(c) == 1:
                    break

    return list(c.values())[0]


T = int(input())

for test_case in range(1, T + 1):
    N, _ = map(int, input().split())
    b = list(map(int, input().split()))
    print(f'#{test_case} {runf(N, b)}')