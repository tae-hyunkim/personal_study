name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],
         ["may", "kein", "brin", "deny"],
         ["kon", "kain", "may", "coni"]]

def solution(name, yearnings, photo):
    # Dictionary 형태로 변환 
    cnt_dict = {names:yearnings for names,yearnings in zip(name,yearning) }
    # 위 Dict cnt_dict = dict(zip(name,yearning)) 으로 쉽게 코딩 가능
    score = [] # 사진 속 인물 합계 담을 List
    for lst in photo: # 사진 추출 
        photo_score = 0 # 사진 점수 초기화 
        for member in lst: # 사진 속 인물 추출 
            if member in name: # 사진 속 인물 중 점수 Matching 가능 인원 추출
                photo_score += cnt_dict[member] # 점수 추가 
        score.append(photo_score)
    return score

print(solution(name,yearning,photo))

# 1줄 코딩 
def solution(name, yearning, photo):
    return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]