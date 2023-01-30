# 폭탄이 연쇄적으로 터지는 것을 막기 위해 visit 배열에만 check 한다.
def solution(board):
    n = len(board)
    visit = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                visit[x][y] = 1
                for i in range(8):
                    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
                    dy = [0, 1, 1, 1, 0, -1, -1, -1]
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if visit[nx][ny] == 0:
                            visit[nx][ny] = 1       
    boom = 0
    for i in range(n):
        boom += sum(visit[i])
    return n * n - boom