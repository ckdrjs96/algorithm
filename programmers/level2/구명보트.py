from collections import deque
def solution(people, limit):
    people.sort()
    people=deque(people)
    cnt=0
    while people:
        avail=limit-people.pop()
        if people and avail >=people[0]:
            people.popleft()
        cnt+=1
    return cnt