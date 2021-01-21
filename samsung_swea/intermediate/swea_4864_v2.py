#Boyer-Moore

def search(short,long):
    ln_s, ln_l = len(short), len(long)
    cnt = 0
    while cnt < ln_l - ln_s + 1:
        #pattern 이 존재를 오른쪽부터 확인, 없으면 틀린 인덱스 저장
        for j in range(ln_s):
            ri = ln_s-1 - j
            if long[cnt+ri] != short[ri]:
                break
        else:
            return 1

        #틀렸을떄의 long의 철자가 short에 있는지 없는지 확인 이동할지
        for k in range(ri):
            #패턴 틀린 위치 앞쪽에 틀렸을 때 문자가 있으면 그 부분까지 이동
            if short[ri-1-k] == long[cnt+ri]:
                cnt += k+1
                break
        # 없으면 틀린부분앞의 칸수+1만큼 뒤로 이동
        else:
            cnt += ri+1

    return 0

T =int(input())
for test_case in range(1, T + 1):
    short = input()
    long = input()
    print(f'#{test_case}',search(short,long))