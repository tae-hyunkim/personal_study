# 프로그래머스 코딩테스트 연습 Level 1 / 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        lst = []

        for j in range(1,int(i**(1/2))+1):
            if i % j == 0 :
                lst.append(j)
                if i // j != j:
                    lst.append(i//j)
        if len(lst) % 2 == 0 :
            answer += i
        else:
            answer -= i
    
    return answer

print("Test 1 : {}".format(solution(13,17)))
print("Test 2 : {}".format(solution(24,27)))