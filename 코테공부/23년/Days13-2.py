# 프로그래머스 코딩테스트 연습 Level 1 / 로또의 최고 순위와 최저 순위

from collections import Counter
def solution(lottos, win_nums):
    answer = []

    cnt_0 = Counter(lottos)[0]
    cnt = 0
    
    for i in lottos:
        if i == 0 :
            continue
        if i in win_nums:
            cnt += 1
    
    if cnt+cnt_0 < 2:
        answer.append(6)
    else:
        answer.append(7-(cnt+cnt_0))

    if cnt < 2:
        answer.append(6)
    else:
        answer.append(7-cnt)

    return answer


print('Test1 : {}'.format(solution([44,1,0,0,31,25],[31,10,45,1,6,19])))
print('Test2 : {}'.format(solution([0,0,0,0,0,0],[38,19,20,40,15,25])))
print('Test3 : {}'.format(solution([45,4,35,20,3,9],[20,9,3,45,4,35])))
