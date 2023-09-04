# 프로그래머스 코딩테스트 연습 Level 2 / 롤케이크 자르기
from collections import Counter
def solution(topping):
    answer = 0
    bro = Counter(topping)
    chul = set()
    for i in topping:
        bro[i] -= 1
        if bro[i] == 0:
            del bro[i]
        chul.add(i)
        if len(bro) == len(chul):
            answer += 1
    return answer

print("Test 1 : {}".format(solution([1,2,1,3,1,4,1,2])))
print("Test 2 : {}".format(solution([1, 2, 3, 1, 4])))