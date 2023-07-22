# 프로그래머스 코딩테스트 연습 Level 1 / 문자열 다루기 기본
import re 
def solution(s):
    return True if len(re.findall(r'[a-zA-Z]',s)) == 0 and (len(s)==4 or len(s) ==6) else False
