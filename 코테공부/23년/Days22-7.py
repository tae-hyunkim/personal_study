# 프로그래머스 코딩테스트 연습 Level 1 / 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''
    lst1 = []
    lst2 = []

    for i in s:
        # 대문자 존
        if i.isupper():
            lst1.append(i)
        else:
            lst2.append(i)
    return ''.join(sorted(lst2,reverse=True)) + ''.join(sorted(lst1,reverse=True))

print("Test1 : {}".format(solution('Zbcdefg')))