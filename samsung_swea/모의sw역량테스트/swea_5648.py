#0.5초에 만나는것을 두배 해주면 이렇게 힘들게 안짜도 된다


from collections import defaultdict
T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    atoms = [list(map(int,input().split())) for _ in range(N)]
    x_list = [atom[0] for atom in atoms]
    x_max, x_min = max(x_list),min(x_list)
    y_list = [atom[1] for atom in atoms]
    y_max, y_min = max(y_list), min(y_list)
    #상(0), 하(1), 좌(2), 우(3)
    moves = [[1,0],[-1,0],[0,-1],[0,1]]
    total_energy = 0
    start = []
    coordinate_dict = defaultdict(list)
    opposites={0:1,1:0,2:3,3:2}

    #0.5초에서 만나는것 확인
    for x, y, dir, energy in atoms:
        coordinate_dict[(x, y)].append([dir, energy])
    for x, y, dir, energy in atoms:
        dy, dx = moves[dir]
        if (x + dx, y + dy) in coordinate_dict and opposites[dir] == coordinate_dict[(x + dx, y + dy)][0][0]:
            atom = coordinate_dict[(x + dx, y + dy)][0]
            total_energy += energy
        else:
            start.append([x, y, dir, energy])
    atoms = start

    while atoms:
        after_atom = []
        coordinate_dict = defaultdict(list)
        for x, y, dir, energy in atoms:
            dy,dx = moves[dir]
            if x_min<= x+dx <=x_max and y_min <= y+dy <= y_max:
                coordinate_dict[(x+dx,y+dy)].append([dir,energy])
        #1초 단위에 일치하는것
        coor_del = []
        for coor,val in coordinate_dict.items():
            if len(val)>1:
                total_energy+= sum([va[1] for va in val])
                coor_del.append(coor)
            else:
                after_atom.append([*coor,*val[0]])
        for coor in coor_del:
            del coordinate_dict[coor]
        print(coordinate_dict,after_atom)
        # #소숫점 단위에 일치
        atoms = []
        for x,y,dir,energy in after_atom:
            dy, dx = moves[dir]
            if (x+dx,y+dy) in coordinate_dict and opposites[dir] == coordinate_dict[(x + dx, y + dy)][0][0]:
                atom = coordinate_dict[(x+dx,y+dy)][0]
                total_energy += energy
            else:
                atoms.append([x,y,dir,energy])

    print(f'#{test_case} {total_energy}')
