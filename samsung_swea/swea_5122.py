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

def I_command(head,idx,data):
    I_node=Node(data)
    I_head=head
    for _ in range (idx):
        I_head=I_head.next

    I_head.next,I_node.next=I_node,I_head.next

    return head

def D_command(head,idx):
    D_head=head
    for _ in range (idx):
        D_head=D_head.next
    D_head.next=D_head.next.next

    return head

def C_command(head,idx,data):
    C_head=head
    for _ in range (idx):
        C_head=C_head.next

    C_head.next.data=data

    return head

#T=1
T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    array = list(map(int, input().split()))
    head= make_listnode(array)
    fuc={'I':I_command,'D':D_command,'C':C_command}


    for _ in range(M):
        to_do = input().split()
        func = fuc[to_do[0]]

        head = func(head, *list(map(int, to_do[1:])))

        # print_head=head
        #
        # while print_head.next:
        #     print_head = print_head.next
        #     print(print_head.data)

    for _ in range(L+1):
        if head.next==None:
            print(f'#{test_case} -1')
            break
        head=head.next
    else: print(f'#{test_case}',head.data)