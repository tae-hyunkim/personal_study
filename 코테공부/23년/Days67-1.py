def solution(s):
    cnt = 0
    cnt1 = 0
    while True:
        cnt2 = s.count('0')
        cnt1 += cnt2
        s = str(bin(len(s) - cnt2))[2:]
        cnt += 1
        if s == '1':
            break 
    return [cnt,cnt1]

print("Test 1 : {}".format(solution('110010101001')))
