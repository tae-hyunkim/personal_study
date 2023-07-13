# 프로그래머스 코딩테스트 연습 Level 1 / 신규 아이디 추천

import re 

def solution(new_id):
    answer = ''
    new_id = re.sub(r'[^a-z0-9\-\._]', '',new_id.lower())

    while new_id.find('..') != -1 :
        new_id = re.sub('\.\.','.',new_id)
    
    if len(new_id) != 0:
        while new_id[0] == '.':
            new_id = new_id[1:]
            if len(new_id) == 0:
                new_id = ''
                break

    if len(new_id) != 0:        
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    if new_id == '':
        new_id = 'a'
    
    if len(new_id) > 15:
        new_id = new_id[:15]
    
    while new_id[-1] == '.':
        new_id = new_id[:-1]
    
    if len(new_id) < 3:
        txt = new_id[-1]
        for i in range(3-len(new_id)):
            new_id += txt

    return new_id

print("Test 1 : {}".format(solution('...!@BaT#*..y.abcdefghijklm')))
print("Test 2 : {}".format(solution("z-+.^.")))
print("Test 3 : {}".format(solution("=.=")))
print("Test 4 : {}".format(solution("123_.def")))
print("Test 5 : {}".format(solution("abcdefghijklmn.p")))
print("Test 6 : {}".format(solution("a.$.a")))
print("Test 7 : {}".format(solution("..................................")))
print("Test 8 : {}".format(solution("a...bAR/56")))