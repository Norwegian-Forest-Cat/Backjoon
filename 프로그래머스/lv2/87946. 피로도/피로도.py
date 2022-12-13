def dfs(level, stamina, clear, dungeons, visit):
    global answer
    answer = max(clear, answer)
    if level == len(dungeons):
        return

    for i in range(len(dungeons)):
        if stamina >= dungeons[i][0] and visit[i] == 0:
            visit[i] = 1
            dfs(level + 1, stamina - dungeons[i][1], clear + 1, dungeons, visit)
            visit[i] = 0

def solution(k, dungeons):
    visit = [0] * len(dungeons)     # 공략한 던전은 방문하지 않음
    dfs(0, k, 0, dungeons, visit)
    return answer

answer = 0