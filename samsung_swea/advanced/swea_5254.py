#T=1
T =int(input())
for test_case in range(1, T + 1):
    N, text = input().split()
    N=int(N)
    substr=set()
    for i in range(len(text)):
        for j in range(len(text),i,-1):
            substr.add(text[i:j])
    substr=list(substr)
    substr.sort()
    ans=substr[N-1]
    print(len(substr))
    print(f'#{test_case}',ans[0],len(ans))
    # print(ord('z'))
    # print(text.index('a'))
    # print(text.index(chr(97)))
    #
    # cnt=0
    # lentext=len(text)
    # for i in range(97,123):
    #     if chr(i) in text:
    #         idx=-1
    #         cnt+=1
    #         while True:
    #             print(idx)
    #             try:
    #                 idx=text[idx+1:].index(chr(i))+idx+1
    #             except ValueError:
    #                 break
    #             cnt+=(lentext-idx)
    #             cnt-=1
    # print(cnt)