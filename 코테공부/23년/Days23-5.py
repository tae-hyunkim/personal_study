# 프로그래머스 코딩테스트 연습 Level 1 / 2016년

def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    ans = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    week = 0
    if a == 1:
        week = b%7 
        return ans[week-1]
    else:
        week += b
        for i in range(a-1):
            week += days[i]
        
        weeks = week%7
        return ans[weeks-1]