# 프로그래머스 코딩테스트 연습 Level 1 / 나머지가 1이 되는 수 찾기 

def solution(n):
    answer = 0
    lst = []
    for i in range(2,int(n**(0.5))+1):
        if n%i == 1 :
            lst.append(i)
            break
    if len(lst) > 0 :
        answer += min(lst)
    else:
        answer += n-1
    return answer


print("Test 1 : {}".format(solution(10)))
print("Test 2 : {}".format(solution(12)))