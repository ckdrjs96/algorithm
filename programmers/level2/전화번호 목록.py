#1. 정렬이용시 뒤엤것만 확인해보면됨
def solution(phone_book):
    phone_book.sort() #1 12 123 13 정렬됨(문자열)
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True

#2. hash 사용 풀이
def solution(phone_book):
    #dictonary 탐색이 hash로 O(1)로 리스트 탐색보다 빠르다
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number[:-1]:
            temp += number
            if temp in hash_map:
                return False
    return True