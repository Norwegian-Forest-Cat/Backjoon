def dfs(level, arr, x, y, visit):
    if level == 2:
        if arr[x][y] == 'P':
            return 0
        else:
            return

    for i in range(4):  # P가 있는 경우 위, 오른쪽, 아래, 왼쪽 확인
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < 5 and 0 <= ny and ny < 5:
            if visit[nx][ny] == 0:
                if level == 0 and arr[nx][ny] == 'P':   # 바로 옆자리가 P라면 0리턴
                    return 0
                # elif arr[nx][ny] == 'X':
                    # visit[nx][ny] = 1
                    # res = dfs(level + 1, arr, nx, ny, visit)
                    # if res == 0:
                    # return
                    # visit[nx][ny] = 0
                elif arr[nx][ny] == 'O' or arr[nx][ny] == 'P':
                    visit[nx][ny] = 1
                    res = dfs(level + 1, arr, nx, ny, visit)
                    visit[nx][ny] = 0
                    if res == 0:
                        return 0


def solution(places):
    answer = []
    visit = [[0] * 5 for _ in range(5)]
    for z in range(5):  # 각 행 확인
        flag = 1
        for x in range(5):  # 각 행의 좌표 확인
            for y in range(5):
                if places[z][x][y] == 'P':     # 사람이 있을 경우 주변 확인
                    visit[x][y] = 1
                    result = dfs(0, places[z], x, y, visit)
                    visit[x][y] = 0
                    if result == 0:
                        flag = 0
        answer.append(flag)

    return answer