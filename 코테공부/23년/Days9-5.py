# 프로그래머스 코딩테스트 연습 Level 1 / 햄버거 만들기

def solution(ingredient):

    if len(ingredient) < 4:
        return 0 

    txt = ''.join([str(i) for i in ingredient])

    test = txt[:3]
    answer = 0 
    for i in txt[3:]:
        test += i 

        while test[-4:] == '1231':
            answer += 1
            test = test[:-4]

    return answer

print("test1 : {}".format(solution([2,1,1,2,3,1,2,3,1])))
print("test2 : {}".format(solution([1,3,2,1,2,1,3,1,2])))