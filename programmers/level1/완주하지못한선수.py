import collections
def solution(participant, completion):
    participant= (collections.Counter(participant))
    for i in completion:
        if participant[i]:
            participant[i] -= 1
    return participant.most_common(1)[0][0]