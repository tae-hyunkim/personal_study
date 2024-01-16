## 효율성 만족 코드... 
### 뜯어보자 
from bisect import bisect_left
from itertools import combinations

def make_all_cases(temp):
    cases = []
    for k in range(5):
        for li in combinations([0, 1, 2, 3], k):
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = make_all_cases(i.split())
        for case in cases:
            if case not in all_people.keys(): all_people[case] = [int(seperate_info[4])]
            else: all_people[case].append(int(seperate_info[4]))

    for key in all_people.keys():
        all_people[key].sort()

    for q in query:
        seperate_q = q.split()
        target = seperate_q[0] + seperate_q[2] + seperate_q[4] + seperate_q[6]
        if target in all_people.keys():
            answer.append(len(all_people[target]) - bisect_left(all_people[target], int(seperate_q[7]), lo=0, hi=len(all_people[target])))
        else:
            answer.append(0)

    return answer
'''
from collections import Counter

def solution(info, query):
    answer = []

    tbl = [i.replace('"','').split(' ') for i in info]
    
    tbls = [{'python' : [], 'java' : [], 'cpp' : []}
            ,{'backend' : [], 'frontend' : []}
            ,{'junior' : [], 'senior' : []}
            ,{'chicken' : [], 'pizza' : []}
            ,[]]

    for i in range(len(tbl)):
        tbls[0][tbl[i][0]].append(str(i))
        tbls[1][tbl[i][1]].append(str(i))
        tbls[2][tbl[i][2]].append(str(i))
        tbls[3][tbl[i][3]].append(str(i))
        tbls[4].append(int(tbl[i][4]))
    all_v = [str(i) for i in range(len(tbl))]

    test_tbl = [i.replace('"','').replace(' and ',' ').split(' ') for i in query]
    
    for tbl_r in test_tbl:
        test_val = []
        for idx,col in enumerate(tbl_r):
            if col == '-':
                test_val = test_val + all_v
            elif idx < 4 :
                test_val = test_val + tbls[idx][col]
            else :
                continue

        check_val = Counter(test_val)
        score_val = int(tbl_r[4])

        values = 0 
        for i,j in check_val.items():
            if j != 4:
                continue
            idxs = int(i)
            if tbls[4][idxs] >= score_val:
                values += 1 
        answer.append(values)
    return answer


print("Test 1 : {}".format(solution([
                                    "java backend junior pizza 150",
                                     "python frontend senior chicken 210",
                                     "python frontend senior chicken 150",
                                     "cpp backend senior pizza 260",
                                     "java backend junior chicken 80",
                                     "python backend senior chicken 50"
                                     ]
                                    , [
                                        "java and backend and junior and pizza 100",
                                       "python and frontend and senior and chicken 200",
                                       "cpp and - and senior and pizza 250",
                                       "- and backend and senior and - 150",
                                       "- and - and - and chicken 100",
                                       "- and - and - and - 150"
                                       ])))
'''