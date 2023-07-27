# 프로그래머스 코딩테스트 연습 Level 2 / 광물 캐기

def solution(picks, minerals):
    answer = 0
    pirodo = [[1,1,1],[5,1,1],[25,5,1]]

    while minerals :
        if 'diamond' in minerals:
            if 'diamond' in minerals[:4]:
                if picks[0] > 0:
                    pick = 0
                    picks[0] = picks[0] - 1 
                elif picks[1] > 0 :
                    pick = 1
                    picks[1] = picks[1] - 1
                else  :
                    pick = 2
                    picks[2] = picks[2] - 1
            
            elif 'iron' in minerals[:4]:
                if picks[1] > 0:
                    pick = 0
                    picks[1] = picks[1] - 1 
                elif picks[0] > 0 :
                    pick = 1
                    picks[0] = picks[0] - 1
                else  :
                    pick = 2
                    picks[2] = picks[2] - 1
            
    return answer