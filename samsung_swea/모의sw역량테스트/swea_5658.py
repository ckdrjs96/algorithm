T = int(input())

for test_case in range(1, T + 1):
    N,K=map(int,input().split())
    n_nums=input()
    n_split = N//4
    all_nums=[]
    for _ in range(n_split):
        num_list=[n_nums[i*n_split:(i+1)*n_split] for i in range(4)]
        all_nums.extend(num_list)
        print(num_list,n_nums)
        n_nums=n_nums[-1]+n_nums[:-1]
    all_nums = list(set(all_nums))
    for i in range(n_split-1,-1,-1):
        all_nums = sorted(all_nums,key=lambda x:x[i],reverse=True)

    print(all_nums)
    dim16={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    for i in range(10):
        dim16[str(i)] = i

    num = all_nums[K-1]
    cnt=0
    for idx,val in enumerate(num):
        cnt += 16**(n_split-idx-1)*dim16[val]
    print(f'#{test_case} {cnt}')

#16진수 -> 10진수 int(num,16)


