# greedy o(N)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # 성립이 안되는 지점이 있다면 그앞은 모두 정답이 될수없다. 따라서 start=i+1
        start, fuel = 0, 0
        for i in range(len(gas)):

            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
            # print(start,fuel)
        return start


#brute force o(N^2) 통과는되지만 매우느리다
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n):
            fuel = 0
            for i in range(n):
                idx = (start + i) % n
                fuel += gas[idx] - cost[idx]
                # print(fuel)
                if fuel < 0:
                    ans = -1
                    break
            # 정답이 반드시 하나라했으므로 찾으면 바로종료
            else:
                return start

        return ans