### tail is not used

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

def insert(M,head,point,tail):
    insert_head=point
    for k in range(M):
        if insert_head.next==None:
            insert_head=head
        insert_head=insert_head.next


    left=insert_head.data
    if insert_head.next==None:
        right=head.next.data
    else: right=insert_head.next.data

    insert_node=Node(left+right)
    insert_head.next,insert_node.next=insert_node,insert_head.next

    return insert_head,tail



#T=1
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    array = list(map(int, input().split()))
    head,tail=make_listnode(array)
    point=head
    for i in range(K):
        point,tail=insert(M,head,point,tail)

    ans=[]
    for _ in range(N+K):
        head = head.next
        ans.append(head.data)
    print(f'#{test_case}', *ans[::-1][:10])