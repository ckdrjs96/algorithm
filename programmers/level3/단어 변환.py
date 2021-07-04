#단어가 하나만 바뀌었는지 확인ㄴ
def isonechange(begin,word):
    cnt=len(begin)
    for i in range(len(begin)):
        if begin[i]==word[i]:
            cnt-=1
    if cnt==1:
        return True
    else: return False

def solution(begin, target, words):
    global ans

    n=len(words)
    ans=n+1
    def dfs(begin, words):
        global ans
        if begin==target:
            ans=min(ans,n-len(words))
            return

        nextword=words.copy()
        for word in words:
            if isonechange(begin,word):
                nextword.remove(word)
                dfs(word,nextword)
                nextword.append(word)


    dfs(begin,words)
    if ans==n+1:
        return 0
    else: return ans