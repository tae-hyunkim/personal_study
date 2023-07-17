# 프로그래머스 코딩테스트 연습 Level 1 / [1차] 다트게임

def solution(dartResult):

    test = ['S','D','T']
    bonus = ['*','#']

    txt = ''
    val = 0
    val1 = 0
    val2 = 0 
    for i in dartResult:
        if i in test:
            if i == 'S': 
                val = val1
                val1 = val2
                val2 = int(txt)
                txt = ''
            if i == 'D':
                val = val1
                val1 = val2
                val2 = int(txt) ** 2
                txt = ''
            if i == 'T':
                val = val1
                val1 = val2
                val2 = int(txt) ** 3
                txt = ''
        elif i in bonus : 
            if i == '*':
                val1 *= 2
                val2 *= 2
                txt = ''
            if i == '#':
                val2 *= (-1)
                txt = ''
        else:
            txt += i 
        # print(val, val1, val2)
    return val + val1 + val2

print("Test 1 : {}".format(solution('1S2D*3T')))
print("Test 2 : {}".format(solution('1D2S#10S')))
print("Test 3 : {}".format(solution('1D2S0T')))
print("Test 4 : {}".format(solution('1S*2T*3S')))
print("Test 5 : {}".format(solution('1D#2S*3S')))
print("Test 6 : {}".format(solution('1T2D3D#')))
print("Test 7 : {}".format(solution('1D2S3T*')))

