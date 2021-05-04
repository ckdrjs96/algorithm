#bfs 풀이 , dfs보다 빠르다.
def solution(numbers, target):
    add=[0]
    for num in numbers:
        plus=list(map(lambda x: x+num,add))
        minus=list(map(lambda x: x-num,add))
        add=plus+minus

    return add.count(target)