# 프로그래머스 코딩테스트 연습 Level 2 / 유사 칸토어 비트열

# 문제 해석 먼저 해보자

## 칸토어 비트열 
## 1인 값에는 11011로 치환
## 0인 값에는 00000로 치환
### 처음 값은 1 
### n = 1일때 1
### n = 2일때 11011
### n = 3일때 11011 11011 00000 11011 11011 
### n = 4일때 (11011 11011 00000 11011 11011) 2번 00000 5번 (11011 11011 00000 11011 11011) 2번 
# 규칙으로 볼때 l ~ r까지 5로 나누었을때 나머지가 2이면 0 아니면 1
# 5로 나눈 값에 몫이 2이면 0 임 
def check(value):
    if value % 5 == 2:
        return False
    if value < 5 :
        return True 
    return check(value//5)
def solution(n, l, r):
    answer = 0

    for i in range(l-1,r):
        if check(i):
            answer += 1
    return answer

print("Test 1 : {}".format(solution(2,4,17)))