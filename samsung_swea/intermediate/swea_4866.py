T = int(input())
remain=['(',')','{','}']
mapping={')':'(','}':'{'}
for test_case in range(1, T + 1):
    sent=input()
    stack=[]
    for i in sent:

        #가로일 경우 판단
        if i in remain:
            if i not in mapping:
                stack.append(i)

            #스택이 비어있거나 제거되지않으면 종료
            elif not stack or stack.pop() != mapping[i]:
                stack.append(i)
                break;

    if not stack:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
