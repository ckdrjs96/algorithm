
N = int(input())
num_list = list(map(int, input().split()))
#[+, - ,x,/]
oper_cnt = list(map(int, input().split())) 
oper_list = ['+', '-' ,'*','//']

global_max = -float('inf')
global_min = float('inf')
def dfs(cnt,already_calculate):
    global global_max, global_min
    if cnt == N:
        # if already_calculate > global_max:
        #     print(log,oper_cnt,already_calculate)
        global_min = min(already_calculate,global_min)
        global_max = max(already_calculate,global_max)
        return
    swap=False
    for i in range(4):
        if oper_cnt[i] > 0 :
            if i==3 and already_calculate <0:
                already_calculate*= -1
                swap = True
            calcul = eval(str(already_calculate) + oper_list[i] + str(num_list[cnt]))
            if i==3 and swap:
                calcul *= -1
                swap = False


            oper_cnt[i] -=1
            dfs(cnt+1,calcul)
            oper_cnt[i] +=1

dfs(1,num_list[0])
print(global_max)
print(global_min)

