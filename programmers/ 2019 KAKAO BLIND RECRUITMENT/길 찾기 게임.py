#설정안해주면 테케 6,7 런타임에러
#파이썬 기본재귀 호출 제한은 1000
#문제에서 트리의 깊이가 1000이하라 했지만 다른 함수와 중첩되면서 1050정도로 하면 통과된다


import sys
sys.setrecursionlimit(10 ** 6)


def left_right(x):
    split_x = x[0][0]
    node = x[0][2]
    left = list(filter(lambda x: x[0] < split_x, x))
    right = list(filter(lambda x: x[0] > split_x, x))
    return node, left, right


def forword(x):
    def split(x):
        if not x:
            return
        node, left, right = left_right(x)
        ans.append(node)
        split(left)
        split(right)

    ans = []
    split(x)
    return ans


def backword(x):
    def split(x):
        if not x:
            return
        node, left, right = left_right(x)
        split(left)
        split(right)
        ans.append(node)

    ans = []
    split(x)
    return ans


def solution(nodeinfo):
    #노드의 번호를 추가
    idx = range(1, len(nodeinfo) + 1)
    a, b = zip(*nodeinfo)
    idx_node = list(zip(a, b, idx))

    #항상 제일 앞이 부모노드를 보장해주기 위한 정렬
    idx_node = sorted(idx_node, key=lambda x: x[0])
    idx_node = sorted(idx_node, key=lambda x: x[1], reverse=True)

    #트리를 좌측 우측으로 나누면서 순회하기
    forward = forword(idx_node)
    backward = backword(idx_node)
    return [forward, backward]