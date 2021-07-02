from collections import Counter
import sys
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def combin(n,p):
    a = factorial(n)/(factorial(p)*factorial(n-p))
    return a
                  
def sumvalue(n,a):
    
    c=[a]
    k=1
    subset=[]    
    while(k<=(n/2)):
        e=[]
        for i in c:
            for j in i:
                check_set = set(i)-{j}
                if check_set not in e:
                    e.append(check_set)
            if len(e) >= combin(n,len(i)):
                break
        c=e
        subset = subset+e
        k+=1
    rest=[set(a)]
    for i in subset:
        rest.append(set(a)-i)

    f=dict(Counter(list(map(sum,subset+rest))))
    return f


n,s= map(int,input().split())
a = list(map(int,input().split()))

g=sumvalue(n,a)
print(g.get(s))
sys.exit()
pos = [i for i in a if i>=0]
neg = [i for i in a if i<0]

neg_cnt=sumvalue(neg)
pos_cnt=sumvalue(pos)

count=0
for key,value in neg_cnt.items():
    for i in pos_cnt.keys():
        if i+key==s:
            count += value * pos_cnt.get(-key+s)


print(count)

