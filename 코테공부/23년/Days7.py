def solution(t,p):
    answer = 0

    p_len = len(p)
    for i in range(len(t) - p_len + 1):
        idx = i 
        idx1 = i + p_len 
        test_val = t[idx:idx1]

        if int(test_val) <= int(p):
            answer += 1

    return answer 

print('test_case1 : {}'.format(solution('3141592','271')))
print('test_case2 : {}'.format(solution('500220839878','7')))
print('test_case3 : {}'.format(solution('10203','15')))