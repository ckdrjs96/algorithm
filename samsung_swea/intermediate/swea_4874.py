def calculate(postfix):
    stack = []
    try:
        for chr in postfix[:-1]:
            if chr.isdigit():
                stack.append(chr)

            else:
                second = stack.pop()
                frist = stack.pop()
                cal=int(eval(frist + chr + second))
                stack.append(str(cal))

    except IndexError:
        return 'error'

    if len(stack)==1:
        return stack[0]
    else:
        return 'error'

#T=1
T =int(input())
for test_case in range(1, T + 1):
    postfix = input().split()
    print(f'#{test_case}',calculate(postfix))
