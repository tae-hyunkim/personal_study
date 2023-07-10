# 프로그래머스 코딩테스트 연습 Level 1 / 둘만의 암호 
def solution(s, skip, index):

    txt2 = 'abcdefghijklmnopqrstuvwxyz'
    txt = ''
    for i in txt2:
        if i in skip:
            continue
        txt += i

    max_len = 26 - len(skip)

    answer = '' 

    for i in s :
        val1 = txt.index(i)  + index 

        if val1 >= max_len :
            val1 = val1 % max_len

        answer +=  txt[val1:val1+1]

    return answer

print('test 1 : {}'.format(solution('aukks','wbqd',5)))