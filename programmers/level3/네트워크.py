def solution(n, computers):
    ans = 0

    def find1(computers):
        for i in range(n):
            for j in range(n):
                if computers[i][j] == 1:
                    return i, j

    def dfs(i, j):
        computers[i][j] = 0
        computers[j][i] = 0

        for k in range(n):
            if computers[j][k] == 1:
                dfs(j, k)

    while True:
        #visited변수 만들어 활용했으면 더 좋을듯
        if sum([sum(computer) for computer in computers]) == 0:
            break
        dfs(*find1(computers))
        print(computers)
        ans += 1

    return ans