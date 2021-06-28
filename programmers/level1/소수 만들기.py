def solution(nums):
    n = len(nums)
    ans = 0
    for i in range(n):
        for j in range(n):
            if i >= j:
                continue
            for k in range(n):
                if j >= k:
                    continue
                if isprime(nums[i] + nums[j] + nums[k]):
                    ans += 1

    return ans


def isprime(x):
    for i in range(2, x // 2):
        if x % i == 0:
            return False
    else:
        return True