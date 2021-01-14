#brute force

def search(pattern,str1):
    pattern_len = len(pattern)

    for i in range(len(str1) - pattern_len + 1):
        if pattern == str1[i:i + pattern_len]:
            return 1
    else:
        return 0


T =int(input())
for test_case in range(1, T + 1):
    pattern = input()
    str1 = input()
    print(f'#{test_case}',search(pattern, str1))