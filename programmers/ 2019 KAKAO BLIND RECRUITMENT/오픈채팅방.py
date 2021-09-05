def solution(record):
    save_dict = dict()
    commands = []

    for recor in record:
        com = recor.split()
        if com[0] == 'Enter' or com[0] == 'Change':
            save_dict[com[1]] = com[2]
        commands.append([com[0], com[1]])

    answer = []
    for command in commands:
        if command[0] == 'Enter':
            answer.append(save_dict[command[1]] + '님이 들어왔습니다.')
        elif command[0] == 'Leave':
            answer.append(save_dict[command[1]] + '님이 나갔습니다.')

    return answer