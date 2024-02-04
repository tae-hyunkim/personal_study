def Change_Text(tmp, uid):
    if tmp == 'Enter':
        return '{}님이 들어왔습니다.'.format(uid)
    if tmp == 'Leave':
        return '{}님이 나갔습니다.'.format(uid)

def solution(record):
    answer = []
    names = {}
    lst = []
    for text in record:
        if text.split(' ')[0] == 'Leave':
            lst.append([text.split(' ')[0],text.split(' ')[1]])
            continue
        tmp, uid, name = text.split(' ')
        if uid in names:
            names[uid] = name
        else:
            names[uid] = name

        if tmp == 'Change':
            continue

        lst.append([tmp,uid])
    
    for chk, Uid in lst:
        answer.append(Change_Text(chk,names[Uid])) 
    return answer

print("Test 1  :{}".format(solution(["Enter uid1234 Muzi", 
                                     "Enter uid4567 Prodo",
                                     "Leave uid1234",
                                     "Enter uid1234 Prodo",
                                     "Change uid4567 Ryan"])))