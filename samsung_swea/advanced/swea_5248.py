#T=1
T =int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr=list(map(int, input().split()))
    mapping=dict()
    for i in range(0,len(arr),2):
        #양방향으로 딕셔너리에 저장
        if arr[i] in mapping: #딕셔너리에 있으면 append
            mapping[arr[i]].append(arr[i + 1])

        else: #없으면 리스트로 value값 생성
            mapping[arr[i]]=[arr[i + 1]]

        if arr[i+1] in mapping:
            mapping[arr[i+1]].append(arr[i])
        else:
            mapping[arr[i+1]] = [arr[i]]

    #몇개의 그릅인지 계산
    ans=[False]*(N+1) #숫자가 그룹안에 있는지 확인
    answer=0
    while mapping:
        stack = list(mapping.keys())[0] #새로운 그룹 첫번째학생
        ans[stack]=True
        stack=[stack]
        while stack: #한 그룹이 다지어지면 종료
            now=stack.pop()
            for i in mapping[now]:
                if ans[i]==False:
                    ans[i]=True
                    stack.append(i)
            del mapping[now]
        answer+=1

    answer=answer+N-sum(ans) #혼자그룹인 학생까지 계산
    print(f'#{test_case}', answer)
