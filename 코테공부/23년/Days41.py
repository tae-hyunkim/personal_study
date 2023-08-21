# 프로그래머스 코딩테스트 연습 Level 2 / 테이블 해시 함수

def solution(data, col, row_begin, row_end):
    answer = 0
    # 데이터 정렬 
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    for i,j in zip(range(row_begin, row_end+1),data[row_begin-1:row_end]):
        value = 0 
        for num in j :
            value += num%i
        answer ^= value

    return answer

print("Test 1 : {}".format(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,2,3)))