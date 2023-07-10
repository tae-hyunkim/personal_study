# 프로그래머스 코딩테스트 연습 Level 1 / 대충 만든 자판
# 자판 관련 문제 > 한방에 통과 

def solution(keymap, targets):
    answer = []

    for target in targets :
        cnt = 0 # 자판 횟수 Cnt 
        for i in range(len(target)): 
            chk = 0 # 문자 잇는지 Check용 
            chk_text = target[i]
            cnt_chk = 999 # targets 길이 최대 100 
            for keys in keymap:
                if chk_text not in keys: # 해당 문자 없으면 다음 keymap 탐지 
                    continue

                if cnt_chk > keys.find(chk_text):
                    cnt_chk = keys.find(chk_text) + 1 # 가장 적은 횟수의 자판 클릭 위한 작업 
            if cnt_chk == 999:
                cnt = -1
                break
            cnt += cnt_chk 
        answer.append(cnt)

    return answer

test1 = solution(['ABACD','BCEFD'],['ABCD','AABB'])
test2 = solution(['AA'],['B'])
test3 = solution(['AGZ','BSSS'],['ASA','BGZ'])

print(test1)
print('--' * 20)
print(test2)
print('--' * 20)
print(test3)