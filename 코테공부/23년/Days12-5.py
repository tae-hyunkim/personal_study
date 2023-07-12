# 프로그래머스 코딩테스트 연습 Level 1 / 숫자 문자열과 영단어 

def solution(s):
    num_chr = {'zero':'0','one':'1','two':'2','three':'3',
               'four':'4','five':'5','six':'6','seven':'7',
               'eight':'8','nine':'9'}
    num_chr_ = num_chr.keys() 
    chr = [str(i) for i in range(10)]
    txt = ''
    txt1 = ''
    for i in s:
        if i in chr:
            txt += i 
            txt1 = ''
            continue
        txt1 += i
        if txt1 in num_chr_:
            txt += num_chr[txt1]
            txt1 = ''
        
    return int(txt)

print('Test 1 : {}'.format(solution("one4seveneight")))
print('Test 2 : {}'.format(solution("23four5six7")))
print('Test 3 : {}'.format(solution("2three45sixseven")))
print('Test 4 : {}'.format(solution("1234")))

# 간략하게 아래와 같이 코드 작성 가능

def solution(s):
    answer = s
    num_chr = {'zero':'0','one':'1','two':'2','three':'3',
               'four':'4','five':'5','six':'6','seven':'7',
               'eight':'8','nine':'9'}
    
    for key,value in num_chr.items():
        answer = answer.replace(key,value)

    return answer 

print('Test 1 : {}'.format(solution("one4seveneight")))
print('Test 2 : {}'.format(solution("23four5six7")))
print('Test 3 : {}'.format(solution("2three45sixseven")))
print('Test 4 : {}'.format(solution("1234")))
