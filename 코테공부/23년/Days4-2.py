# 프로그래머스 코딩테스트 연습 Level 1 / 카드 뭉치
# 카드 뭉치 2개로 원하는 멘트 만들기 
## 다듬어야 하는 부분 > 목표로 하는 Goal의 갯수는 결국 cards1, cards2의 길이와 동일
# pop 함수 
def solution(cards1, cards2, goal):

    card1 = cards1[0]
    card2 = cards2[0]
    for check in goal:

        if check == card1:
            cards1.remove(check)
            if len(cards1) == 0 :
                card1 = ''
            else:
                card1 = cards1[0]

        elif check == card2:
            cards2.remove(check)
            if len(cards2) == 0 :
                card2 = ''
            else:
                card2 = cards2[0]
        
        else:
            return 'No'
        
    return 'Yes'


test1 = solution(['i','drink','water'],['want','to'],['i','want','to','drink','water'])
test2 = solution(['i','water','drink'],['want','to'],['i','want','to','drink','water'])
print(test1)
print('--'*20)
print(test2)