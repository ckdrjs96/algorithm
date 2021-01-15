T =int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    mapping=dict()
    for chr in str2:
        if chr in str1:
            if chr in mapping:
                mapping[chr]+=1
            else:
                mapping[chr]=1
    print(f'#{test_case}', max(mapping.values()))

