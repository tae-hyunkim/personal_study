# 프로그래머스 코딩테스트 연습 Level 1 / 성격 유형 검사하기

def solution(survey, choices):
    answer = ''
    num_dict = {'R':0, 'C':0, 'J':0, 'A':0}
    chr_dict = {'T':'R','F':'C','M':'J','N':'A'}
    chr_dict2 = {'R':'T','C':'F','J':'M','A':'N'}

    for i,j in zip(survey,choices):
        if i[0] in num_dict:
            num_dict[i[0]] = num_dict[i[0]] - (j - 4)
        else:
            num_dict[chr_dict[i[0]]] = num_dict[chr_dict[i[0]]] + (j - 4) 
    
    for texts, nums in num_dict.items():
        if nums < 0 :
            answer += chr_dict2[texts]
        else:
            answer += texts
    return answer

print('test1 : {}'.format(solution(["AN", "CF", "MJ", "RT", "NA"],[5,3,2,7,5])))
print('test2 : {}'.format(solution(["TR", "RT", "TR"],[7,1,3])))