def solution(s):
    answer = []
    lst = s[2:-2].split('},{') 
    cnt = {}
    for i in lst:
        cnt[i] = i.count(',')+1

    for i,j in sorted(cnt.items(),key= lambda item : item[1]):
        for val in i.split(','):
            if int(val) not in answer:
                answer.append(int(val))

    return answer

print("Test 1 : {}".format(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")))
print("Test 2 : {}".format(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")))