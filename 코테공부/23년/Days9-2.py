# 프로그래머스 코딩테스트 연습 Level 1 / 기사단원 무기 

# 약수 구하는 Function 

def solution(number, limit, power):
    answer = 0
    for num in range(1,number+1):
        cnt = 0 
        for i in range(1,int(num**(1/2))+1):
            if num % i == 0 : # 약수 라면 나머지 0 
                if i * i == num: # i가 number의 제곱근일때
                    cnt += 1
                else:
                    cnt += 2
        if cnt > limit:
            answer += power 
        else:
            answer += cnt
    return answer

print('Test1 : {}'.format(solution(5,3,2)))
print('Test2 : {}'.format(solution(10,3,2)))