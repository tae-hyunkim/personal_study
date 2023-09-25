# 프로그래머스 코딩테스트 연습 Level 2 / k진수에서 소수 개수 구하기 

def solution(n, k):
    answer = 0

    # n 값을 k진수로 변환
    chk = ''
    while n > 0 :
        n,mod = divmod(n,k)
        chk += str(mod)
    chk = chk[::-1]
    check_val = chk.split('0')
    
    # 변환된 값의 소수 chk 
    for val in check_val :
        if val == '':
            continue
        number = int(val)
        chk_val = 1
        for i in range(2,int(number**(1/2))+1):
            if number%i==0:
                chk_val = 0 
                break

        if chk_val == 1 and number != 1:
            answer += 1

    return answer

print("Test 1 : {}".format(solution(437674,3)))