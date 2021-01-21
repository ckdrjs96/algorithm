T = int(input())

for test_case in range(1, T + 1):
    n,m=map(int,input().split())
    a=input().split()
    print(f'#{test_case} {a[(m%n)]}')
