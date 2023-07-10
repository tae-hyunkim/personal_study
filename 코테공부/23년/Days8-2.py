# 프로그래머스 코딩테스트 연습 Level 1 / 문자열 나누기
def solution(s):
    answer = 0

    idx1 = ''
    num1, num2 = 1, 0 

    for i,txt in enumerate(s):
        if idx1 == '':
            idx1 = txt
                
        elif idx1 != txt:
            num2 += 1
            
        else :
            num1 += 1 

        if num1 == num2:
            answer += 1
            idx1 = '' 
            num1, num2 = 1, 0
        elif i == len(s) - 1 and num2 != num1:
            answer += 1

    if num1+num2 == len(s):
        answer = 1
    
    return answer 

print("test1 : {}".format(solution('banana')))
print("test2 : {}".format(solution('abracadabra')))
print("test3 : {}".format(solution('aaabbaccccabba')))
print("test chk1 : {}".format(solution('aabababababab')))
print("test chk2 : {}".format(solution('abaa')))
print("test chk3 : {}".format(solution('abaab')))