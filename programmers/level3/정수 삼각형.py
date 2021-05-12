def solution(triangle):
    n=len(triangle)
    add=triangle[n-1]
    for row in range(n-2,-1,-1):
        new=[]
        for col in range(row+1):
            #현재값과 자식노드 왼쪽 오른쪽의 최댓값을 저장
            new.append(triangle[row][col]+max(add[col],add[col+1]))
        # 하위문제를 모두 풀어 add에 저장
        add=new

    return add[0]