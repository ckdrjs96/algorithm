def many(num,cards):
    card = [0] * 10
    for car in cards:
        card[int(car)] += 1
    card.reverse()
    print(f'#{test_case}',9 - card.index(max(card)),max(card))


T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    cards = input()
    many(num,cards)