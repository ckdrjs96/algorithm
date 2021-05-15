def solution(k, room_number):
    ans = []
    hash_map={}

    for room in room_number:
        if room in hash_map:
            hint=room
            collect=[]
            while True:
                if hint not in hash_map:
                    hash_map[hint]=hint+1
                    ans.append(hint)
                    break
                collect.append(hint)
                hint=hash_map[hint]
            for coll in collect:
                hash_map[coll]=hint+1
        else:
            ans.append(room)
            hint=room+1
            while True:
                if hint not in hash_map:
                    hash_map[room]=hint
                    break
                hint=hash_map[hint]


    return ans