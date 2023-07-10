# 프로그래머스 코딩테스트 연습 Level 1 / 숫자 짝궁

from collections import Counter
def solution(X, Y):
    answer = ''
    x = Counter(X)
    y = Counter(Y)
    a = 0
    for i in range(9,-1,-1):
        val = min(y[str(i)],x[str(i)])
        answer += str(i) * val
        if val == 0 :
            a += 1 
    if a == 10:
        return str(-1)
    if answer[-1] == '0' and answer[0]=='0':
        return '0'
    return answer

print('Test 1 : {}'.format(solution('100','2345')))
print('Test 2 : {}'.format(solution('100','203045')))
print('Test 3 : {}'.format(solution('100','123450')))