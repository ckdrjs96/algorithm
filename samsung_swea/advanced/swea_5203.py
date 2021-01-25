def babygin(ans):
    for i in range(10):
        #triplet 확인
        if ans[i]==3:
            return 1
        #run 확인
        if i<8:
            if ans[i] >0 and ans[i+1]>0 and ans[i+2]>0:
                return 1
    else:
        return 0

#T=1
T =int(input())
for test_case in range(1, T + 1):
    arr=list(map(int, input().split()))
    #초기 각 2개값 입력
    p1=[0]*10
    p1[arr[0]]+=1
    p1[arr[2]]+=1
    p2=[0]*10
    p2[arr[1]]+=1
    p2[arr[3]]+=1



    winner=0

    for i in range(4,12,2):
        p1[arr[i]]+=1
        if babygin(p1)==1:
            winner=1
            break

        p2[arr[i+1]]+=1
        if babygin(p2)==1:
            winner=2
            break
    print(f'#{test_case}',winner)
