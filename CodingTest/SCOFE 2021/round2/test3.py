import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
# 상하위 트리 만들기
tree = [i for i in range(N + 1)]
height = [0] * (N + 1)
for _ in range(N - 1):
    up, down = map(int, input().split())
    tree[down] = up
    height[down] = height[up] + 1


def find_root(x, val):
    global cnt
    if cnt < 0:
        return False
    cnt -= 1

    if tree[x] == val:
        return True
    elif tree[x] == x:
        return False
    else:
        return find_root(tree[x], val)


# 상하위 관계 확인
for _ in range(Q):
    up, down = map(int, input().split())
    cnt = height[down] - height[up]

    if cnt > 0:
        if find_root(down, up):
            print('yes')
        else:
            print('no')
    else:
        print('no')
    #
    # if cnt>0:
    #     if find_root(down,up):
    #         print('yes')
    #     else:
    #         print('no')
    # else:
    #     print('no')