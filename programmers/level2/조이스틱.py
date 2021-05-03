
def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) ==0:
            break
        left, right = 1, 1
        while make_name[idx - left] ==0:
            left +=1
        while make_name[idx + right] ==0:
            right +=1
        #좌우로 가야되는 가장 가까운 쪽으로 움직이기 같으면 왼쪽우선
        answer += left if left < right else right
        idx += -left if left < right else right
        print(answer,idx)
    return answer
