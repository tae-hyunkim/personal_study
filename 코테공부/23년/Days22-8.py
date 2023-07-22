# 프로그래머스 코딩테스트 연습 Level 1 / 문자열 내 p와 y의 개수

from collections import Counter
def solution(s):
    answer = True
    chk = s.lower()
    if 'p' not in chk and 'y' not in chk:
        return True
    
    txt = Counter(chk)

    if txt['p'] == txt['y']:
        return True
    else:
        return False