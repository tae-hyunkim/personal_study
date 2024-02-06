def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        # 하나씩 데이터를 받아와서, 금번 숫자가 직전 값보다 크면 숫자를 제거한다. 
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])


print("Test1 : {}".format(solution("1924",2)))
print("Test2 : {}".format(solution("1231234",3)))
print("Test3 : {}".format(solution("4177252841",4)))