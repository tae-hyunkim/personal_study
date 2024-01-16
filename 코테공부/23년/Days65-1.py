def solution(s):
    answer = 0

    s_keys = {')':'(', '}':'{',']':'['}

    for i in range(len(s)):
        stack = []

        rotated = s[i:] + s[:i]

        for b in rotated:

            if b in ')]}':

                if stack and (stack[-1]==s_keys[b]):
                    stack.pop()
                    continue 

                else:
                    break 
            stack.append(b)
        else: 
            if not stack:
                answer += 1 
    return answer

print("Test 1 : {}".format(solution("[](){}")))
print("Test 2 : {}".format(solution("}]()[{")))
print("Test 3 : {}".format(solution("[)(]")))
print("Test 4 : {}".format(solution("}}}")))