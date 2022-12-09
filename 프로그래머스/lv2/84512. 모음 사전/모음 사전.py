cnt, answer = 0, 0  # 전역변수 선언

def dfs(level, arr, word2):
    global cnt, answer
    data = ['A', 'E', 'I', 'O', 'U']

    if arr == word2:
        answer = cnt
        return

    if level == 5:      # 길이 5가 되면 return
        return

    for i in range(5):
        arr.append(data[i])
        cnt += 1        # 다음 dfs 들어가기 전에 카운트
        dfs(level + 1, arr, word2)
        arr.pop()

def solution(word):
    word2 = list(word)
    dfs(0, [], word2)
    return answer
