# 프로그래머스 코딩테스트 연습 Level 1 / 핸드폰 번호 가리기

def solution(phone_number):
    return '*' * (len(phone_number) -4 ) + phone_number[-4:]

print("test 1 : {}".format(solution("01033334444")))
print("test 2 : {}".format(solution("026787777")))
