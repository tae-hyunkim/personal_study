# 프로그래머스 코딩테스트 연습 Level 2 / 모음사전
# A E I O U <- 6진수로써 작업을 진행 

def solution(word):
    answer = 0
    lst = [781,156,31,6,1]
    words = ['A','E','I','O','U']

    for string in range(len(word)):
        answer += (words.index(word[string])) * lst[string]
        
    answer += len(word)
    return answer

print("Test 1 : {}".format(solution('AAAAE')))
