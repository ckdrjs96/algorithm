

#T=1
T =int(input())
for test_case in range(1, T + 1):
    N,six=input().split()
    #quotient,remainder=divmod(n,2)
    print(f'#{test_case} ',end='')

    for i in six:
        #16진수의 A~F
        if i.isalpha():
            num=ord(i)-55
        else: num=int(i)

        ans = []
        for _ in range(4):
            num,remainder=divmod(num,2)
            ans.append(remainder)

        for bit in ans[::-1]:
            print(bit,end='')
    print()