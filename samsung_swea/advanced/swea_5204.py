#병합정렬
def merge(left,right):
    global cnt

    if left[-1] >right[-1]:
        cnt+=1

    mergelist=[]
    left_i,right_i,i=0,0,0
    #둘중 하나라도 다사용하면 종료
    while left_i <len(left) and right_i < len(right):
        # 왼쪽이 더 작으면 추가
        if left[left_i] < right[right_i]:
            mergelist.append(left[left_i])
            left_i+=1
        #오른쪽이 더작으면 추가
        else:
            mergelist.append(right[right_i])
            right_i+=1
        i += 1

    #왼쪽만 남았을때
    if left_i !=len(left):
        mergelist+=left[left_i:]
    #오른쪽만 남았을떄
    if right_i !=len(right):
        mergelist+=right[right_i:]


    return mergelist

def two_split(arr):

    n=len(arr)
    if n==1:
        return arr

    left=arr[:n//2]
    right=arr[n//2:]
    a=two_split(left)
    b=two_split(right)

    return merge(a,b)



#T=1
T =int(input())
for test_case in range(1, T + 1):
    N=int(input())
    arr=list(map(int, input().split()))
    cnt=0

    print(f'#{test_case}',two_split(arr)[N//2],cnt)