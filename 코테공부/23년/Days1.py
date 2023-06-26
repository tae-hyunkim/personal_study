players = ["mumu", "soe", "poe", "kai", "mine"]

callings = ["kai", "kai", "mine", "mine"]

for i in callings:
    # Dict 형태로 변환 (값 자체가 순위)
    player = {player : i for i,player in enumerate(players)}

    for call in callings:
        # 불린 값의 Index 추출, 추월 Index 추출
        # Dict의 VALUE를 가져와서 작업하기 때문에 List Index보다 시간이 적게 소요됨
        idx1, idx2 = player[call] - 1, player[call]

        players[idx1], players[idx2] = players[idx2], players[idx1]

        player[players[idx1]], player[players[idx2]] = player[players[idx1]] - 1, player[players[idx2]] + 1

print(players)