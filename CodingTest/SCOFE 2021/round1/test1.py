#정답
#표기법을 이상하게해서 코드 길어졌다.
#fstring {val:02} 0으로 2자리수 맞추기

N=int(input())
between_st=0
between_end=24*60
for _ in range(N):
    start,end=input().split(' ~ ')
    # print(start,end)
    start_h,start_m=map(int,start.split(':'))
    end_h, end_m = map(int,end.split(':'))
    if end_h*60+end_m < between_st or between_end < start_h*60+start_m:
        print(-1)
        break
    between_st=max(between_st,start_h*60+start_m)
    between_end=min(between_end,end_h*60+end_m)
    # print(between_st,between_end)
else:
    ans_st_m=between_st%60
    ans_end_m=between_end%60
    # if 0<=ans_st_m<10:
    #     ans_st_m='0'+str(between_st%60)
    # if 0<=ans_end_m<10:
    #     ans_end_m='0'+str(between_end%60)
    # if 0<=between_st//60<10:
    #     between_st='0'+str(between_st//60)
    # else:
    #     between_st=between_st//60
    # if 0<=between_end//60<10:
    #     between_end='0'+str(between_end//60)
    # else:
    #     between_end=between_end//60

    print(f'{between_st//60:02}:{ans_st_m:02} ~ {between_end//60:02}:{ans_end_m:02}')