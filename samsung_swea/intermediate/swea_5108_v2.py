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
    return head

def insert(index,num,head):
    new=Node(num)
    insert_head=head
    for _ in range(index):
        insert_head=insert_head.next
    insert_head.next,new.next=new,insert_head.next


    return head

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    array = list(map(int, input().split()))

    head=make_listnode(array)
    for _ in range(M):
        index, num = map(int, input().split())
        head=insert(index,num,head)

    for _ in range(L+1):
        head=head.next
    print(f'#{test_case}',head.data)

