def bfs(x, y, team):
    global visit, arr
    visit[x][y] = 1
    q = [(x, y)]
    score = 1

    while q:
        x, y = q.pop(0)
        for i in range(4):
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if visit[nx][ny] == 0 and arr[nx][ny] == team:
                    visit[nx][ny] = 1
                    score += 1
                    q.append((nx, ny))
    return score

N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
visit = [[0] * N for _ in range(M)]
score_B, score_W = 0, 0

for x in range(M):  # 행
    for y in range(N):  # 열
        if arr[x][y] == 'B' and visit[x][y] == 0:
            score = bfs(x, y, 'B')
            score_B += score ** 2
        elif arr[x][y] == 'W' and visit[x][y] == 0:
            score = bfs(x, y, 'W')
            score_W += score ** 2

print(score_W, score_B)