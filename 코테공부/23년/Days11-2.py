# 프로그래머스 코딩테스트 연습 Level 1 / 신고 결과 받기 
## 다시 풀어보기 
def solution(id_list, report, k):
    
    report = list(set(report))

    dict_lst = [0 for i in id_list]
    name_lst = [[] for i in id_list]

    for text in report:

        name1, name2 = text.split(' ')

        dict_lst[id_list.index(name2)] += 1
        name_lst[id_list.index(name1)].append(name2)
    
    mail_list = [0 for i in id_list]
    
    for i in range(len(name_lst)):
        for j in range(len(name_lst[i])):
            if dict_lst[id_list.index(name_lst[i][j])] >= k:
                mail_list[i] += 1
            

    return mail_list


print("Test 1 : {}".format(solution(["muzi", "frodo", "apeach", "neo"],
                                    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
                                    2)))

print("Test 2 : {}".format(solution(["con", "ryan"],
                                    ["ryan con", "ryan con", "ryan con", "ryan con"],
                                    3)))


