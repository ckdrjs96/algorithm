
#T=1
T =int(input())
for test_case in range(1, T + 1):
    N = int(input())
    start=[]
    end=[]
    for _ in range(N):
        s,e=map(int,input().split())
        start.append(s)
        end.append(e)
    end_or=end[::]
    end.sort()


    cnt=0
    finish=None
    #끝난시간 순서대로 탐색
    for fin in end:
        #맨처음 초기값
        if finish==None:
            finish=fin
            cnt+=1
        else:
            #끝난시간이후에 시작하면
            if start[end_or.index(fin)] >= finish:
                finish=fin
                cnt+=1

        #사용하였으면 시작시간 끝난시간에서 모두제거
        del start[end_or.index(fin)]
        end_or.remove(fin)
    print(f'#{test_case}',cnt)

