#중위순회 inorder traversal

def inorder_traversal(node):
    global in_num

    if node > N:
        return

    #왼쪽 서브트리로 이동
    inorder_traversal(node*2)
    #현재 서브티리의 루트이면 값저장
    in_num += 1
    binary_tree[node]=in_num
    #오른쪽 서브트리로 이동
    inorder_traversal(node*2+1)

#T=1
T =int(input())
for test_case in range(1, T + 1):
    N = int(input())
    binary_tree=[None]*(N+1)

    in_num=0
    inorder_traversal(1)
    print(f'#{test_case}',binary_tree[1],binary_tree[N//2])