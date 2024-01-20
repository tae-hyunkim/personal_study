from collections import deque

def solution(expression):
    # 6개의 연산자 우선순위
    formul = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    answer = 0      # 리턴하는 결과값
    
    arr = []     # 수식을 저장하는 베열.
    num = ''    # 숫자를 판별.
    
    # 문자열인 수식을 배열에 저장
    for ch in expression:
        if ch.isnumeric():
            num += ch
        else:
            arr.append(int(num)) # 숫자 저장
            num = '' # 숫자 초기화
            arr.append(ch) # 연산자 추가 

    arr.append(int(num))

    for formular in formul:
        queue = deque(arr)  # 숫자 삽입 
        
        for operator in formular: # 연산자 추출 

            calculate = deque([])

            while queue:
                chk = queue.popleft()   # Queue에 값을 하나씩 추출

                if chk == operator:     # 만약 연산자일때 연산자마다 계산
                    if chk == '+':

                        num1 = calculate.pop()  # 연산자 이전 숫자 추출
                        num2 = queue.popleft()  # 연산자 다음 숫자 추출
                        calculate.append(num1+num2) # 연산자 계산
                    elif chk == '-':
                        num1 = calculate.pop()  # 연산자 이전 숫자 추출
                        num2 = queue.popleft()  # 연산자 다음 숫자 추출
                        calculate.append(num1 - num2)   # 연산자 계산
                    else:
                        num1 = calculate.pop()  # 연산자 이전 숫자 추출
                        num2 = queue.popleft()  # 연산자 다음 숫자 추출
                        calculate.append(num1 * num2)   # 연산자 계산
                else:
                    calculate.append(chk)   # 숫자인 경우 저장

            queue = calculate.copy()    # 완료된 수식을 다시 Queue에 저장하여 계산

        result_num = queue.pop()    # 수식 최종값
        answer = max(answer, abs(result_num))    # 수식값의 절대값이 크다면 결과값 수정


    return answer   # 결과값 출력

print("Test 1 : {}".format(solution("100-200*300-500+20")))
print("Test 1 : {}".format(solution("50*6-3*2")))