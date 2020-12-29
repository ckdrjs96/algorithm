T = int(input())
for test_case in range(1, T + 1):
    sent=input()
    stack=[]
    for s in sent:
        if not stack:
            stack.append(s)
        elif stack[-1]==s:
            stack.pop()
        else:
            stack.append(s)
    print(f'#{test_case} {len(stack)}')
