class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        table={')':'(','}':'{',']':'['}
        
        for char in s:
            print(char)
            if char not in table:
                stack.append(char)
            elif not stack:
                return False
            elif stack[-1]==table[char]:
                stack.pop()
            else:
                stack.append(char)

                
            #print(f'stack:{stack}')
        
        return not stack
