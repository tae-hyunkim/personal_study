# 문자열 압축

def solution(s):
    answer = len(s)
    ans = len(s)
    for i in range(1, ans//2 + 1): # 압축할꺼기 때문에 절반까지반 Chk 
        test, idx = '', 0 # Test하고자 하는 idx Check 

        while idx < ans: # Text Chk 범위가 input s 길이까지 Chk 
            text, n = s[idx:idx+i], 1 # i길이만큼 반복되는지 Chk 
            while text == s[idx+i:idx+i+i]: # 다음 문장 Chk 
                idx, n = idx+i, n+1 # 같은경우 n+1을 해서 문장 제작 
            test, idx = test + ((str(n)+text) if n != 1 else text), idx+i  # 압축결과 자료 제작 
        answer = len(test) if len(test) < answer else answer # Chk 
    return answer