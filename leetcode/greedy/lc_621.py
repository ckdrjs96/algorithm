class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            for task, _ in counts.most_common(n + 1):
                sub_count += 1
                result += 1

                # 값을 하나씩 줄이기
                counts.subtract(task)
                # value가 0이하가 되면 counts에서 제거
                counts += collections.Counter()

            # counter가 비면 종료(마지막 부분이므로 idle부분 추가계산 없이 종료)
            if not counts:
                break

            # idle 부분을 추가(for문에서 n+1개에서 못뽑힌만큼 더해주기)
            result += n + 1 - sub_count

        return result