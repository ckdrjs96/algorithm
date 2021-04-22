class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        expression = expression.replace('+', ' + ')
        expression = expression.replace('-', ' - ')
        expression = expression.replace('*', ' * ')
        expression = expression.split()

        def recurse(expression):
            if len(expression) == 1:
                return expression

            ans = []
            for i in range(len(expression) // 2):
                left = recurse(expression[:2 * i + 1])
                right = recurse(expression[2 * i + 2:])
                # print(left,right)
                for l in left:
                    for r in right:
                        ans.append(eval(str(l) + expression[2 * i + 1] + str(r)))

            return ans

        return recurse(expression)

