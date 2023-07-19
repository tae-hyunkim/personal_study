# 프로그래머스 코딩테스트 연습 Level 1 / 비밀지도

def solution(n, arr1, arr2):
    answer = []
    lst1 = []
    lst2 = []

    for i in arr1 :
        txt = ''
        for j in range(n) :
            if i > 0 :
                txt += str(i%2)

                i = i // 2
            else:
                txt += '0' 

        lst1.append(txt[::-1])

    for i in arr2:
        txt = ''
        for j in range(n):
            if i > 0 :
                txt += str(i%2)
                i = i // 2
            else:
                txt += '0'
        lst2.append(txt[::-1])

    for i in zip(lst1,lst2):
        txt = ''
        for j in zip(i[0],i[1]):
            if j[0] == '0' and j[1] == '0':
                txt += ' '
            else:
                txt += '#'
        answer.append(txt)
    
    return answer

print("test1 : {}".format(solution(5,[9, 20, 28, 18, 11]
                                   ,	[30, 1, 21, 17, 28])))