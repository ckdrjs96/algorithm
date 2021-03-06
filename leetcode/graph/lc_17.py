class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}

        def graph(i):
            if i == len(digits):
                return

            now = mapping[int(digits[i])]
            ans2 = []
            for char in now:
                next_chr_list = graph(i + 1)
                if next_chr_list:
                    for next_chr in next_chr_list:
                        ans = char + next_chr
                        ans2.append(ans)
                else:
                    ans = char
                    ans2.append(ans)
            return ans2

        return graph(0)