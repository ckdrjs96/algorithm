def solution(skill, skill_trees):
    stack = list(skill)
    stack_o = stack[::-1]

    def check(skill_tree, stack_o):
        stack = stack_o.copy()

        for tree in skill_tree:
            if not stack:
                return True
            if tree == stack[-1]:
                stack.pop()
            elif tree in stack:
                return False
        return True

    ans = 0
    for skill_tree in skill_trees:
        if check(skill_tree, stack_o):
            ans += 1

    return ans