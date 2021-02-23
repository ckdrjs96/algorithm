#T=1
T =int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A=[input() for _ in range(N)]
    B = [input() for _ in range(M)]

    cnt=0
    for text in B:
        for a_text in A:
            #접두어은 앞만 비교하면 되므로 해당길이만큼 슬리이싱하여 비교
            if text==a_text[:len(text)]:
                cnt+=1
                break


    print(f'#{test_case}',cnt)