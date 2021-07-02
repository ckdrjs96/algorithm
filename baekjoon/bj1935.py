import sys

a='ABCD*+*'
print(a[-1])
sys.exit()
stack=[]
operator=[]
ans=[]
ans_char=''
for char in a:
    if char.isalpha() == True:
        stack.append(char)
    elif char.isalpha() == False and not ans:
        last=stack.pop()
        first=stack.pop()
        ans_char=str(first) + str(char) + str(last)
    elif char.isalpha() == False and ans:
        ans_char=str(stack.pop())+str(char)+str(ans_char)
print(ans)