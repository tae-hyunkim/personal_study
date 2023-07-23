# 프로그래머스 코딩테스트 연습 Level 1 / 가운데 글자 가져오기

def solution(s):
    if len(s)%2 == 1:
        return s[len(s)//2]
    else:
        return s[len(s)//2 - 1 : len(s)//2+1]