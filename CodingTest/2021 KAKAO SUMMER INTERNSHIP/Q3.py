def solution(n, k, cmd):
    now=k
    deleted=[]
    cell=n
    size=[i for i in range(n)]
    for cm in cmd:
        if cm=='C':
            idx=size.pop(now)
            deleted.append(idx) #삭제된 원래 위치
            cell-=1
            #삭제하는 행이 가장 마지막 행일때
            if now==cell:
                now-=1
        elif cm=='Z':
            redo=deleted.pop()
            size.append(redo)
            size.sort()
            cell+=1
            if size.index(redo) <= now:
                now+=1

        else:
            u_d,cnt=cm.split()
            if u_d=='U':
                now-=int(cnt)
            else : now+=int(cnt)
        # print(now,cell,size,deleted)
    answer = ['X']*(n)
    for i in size:
        answer[i]='O'
    # print(size)
    return ''.join(answer)

print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))