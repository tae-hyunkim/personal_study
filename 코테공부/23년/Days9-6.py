# 프로그래머스 코딩테스트 연습 Level 1 / 옹알이(2)

def solution(babbling):
    answer = 0
    lst = ['aya','ye','woo','ma']
    first_txt = ['a','y','w','m']
    lst_dict = {i[0]:len(i) for i in lst}
    for txt in babbling:
        cnt = 1
        before = ''
        while len(txt) > 0 :
            if txt[0] in first_txt:
                if txt[:lst_dict[txt[0]]] in lst and before != txt[:lst_dict[txt[0]]]:
                    before = txt[:lst_dict[txt[0]]]
                    txt = txt[lst_dict[txt[0]]:]
                    
                else:
                    cnt = 0
                    before = ''
                    break
            else:
                cnt = 0 
                before = ''
                break
        if cnt > 0 :
            answer += 1

    return answer

print("test 1 : {}".format(solution(['aya','yee','u','maa'])))
print("test 2 : {}".format(solution(['ayaye','uuu','yeye','yemawoo','ayaayaa'])))
print("test 3 : {}".format(solution(['yeye','yeye'])))
print("test 4 : {}".format(solution(['yemawoo'])))
print("test 5 : {}".format(solution(['ayayeye'])))