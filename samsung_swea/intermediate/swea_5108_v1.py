### use list

T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    array = list(map(int, input().split()))

    for _ in range(M):
        index, num = map(int, input().split())
        array = array[:index] + [num] + array[index:]
        # array.insert(*map(int, input().split()))

    print(f'#{test_case} {array[L]}')