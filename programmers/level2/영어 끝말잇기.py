def solution(n, words):
    stack=[words[0]]
    for i , word in enumerate(words[1:],2):
        #같은단어 확인
        if word in stack:
            break
        #끝말이어진는지 확인
        if stack[-1][-1] !=word[0]:
            break
        stack.append(word)
    else:
        return [0,0]

    return [(i-1)%n+1,(i-1)//n+1]