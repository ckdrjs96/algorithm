###use listnode


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def make_listnode(new):
    head = Node(None)
    tail = head
    for x in new:
        tail.next = Node(x)
        tail = tail.next

    return head, tail


def sum_list(sumlist_head, sumlist_tail, new):
    new_head, new_tail = make_listnode(new)
    check_head = sumlist_head
    while check_head.next:
        if check_head.next.data > new_head.next.data:
            check_head.next, new_tail.next = new_head.next, check_head.next

            return sumlist_head, sumlist_tail
        check_head = check_head.next

    sumlist_tail.next = new_head.next
    return sumlist_head, sumlist_tail


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    for i in range(M):
        new = list(map(int, input().split()))
        if i > 0:
            sumlist_head, sumlist_tail = sum_list(sumlist_head, sumlist_tail, new)

        else:
            sumlist_head, sumlist_tail = make_listnode(new)

    ans = []
    head_print = sumlist_head
    for _ in range(i * M + M):
        head_print = head_print.next
        ans.append(head_print.data)
    print(f'#{test_case}', *ans[::-1][:10])
