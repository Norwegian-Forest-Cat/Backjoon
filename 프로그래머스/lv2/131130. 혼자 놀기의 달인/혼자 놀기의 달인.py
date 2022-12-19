# 혼자 놀기의 달인

def solution(cards):
    visit = [0] * len(cards)
    cnt = 0  # 상자의 개수
    box = [[]]

    for i in range(len(cards)):
        index = i
        while sum(visit) < len(cards):      # 모든 상자를 분류 할때까지 확인
            if visit[index] == 0:
                visit[index] = 1
                box[cnt].append(cards[index])
                index = cards[index] - 1

            else:         # index 값이 끝났다면
                box.append([])
                cnt += 1  # 각 상자를 채웠다고 표시
                break

    box.sort(key=len, reverse=True)      # 상자가 많은 개수대로 정렬

    if len(box) >= 2:
        return len(box[0]) * len(box[1])
    else:
        return 0    # 박스가 1그룹만 있으면 0 반환