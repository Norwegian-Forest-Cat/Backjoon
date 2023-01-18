from itertools import permutations

def solution(babbling):
    text = ["aya", "ye", "woo", "ma"]
    word = list(permutations(text))
    for x in range(4):      # 4가지 단어 조합
        word = list(permutations(text, x))
        for y in range(len(word)):      # word의 개수
            new = ''
            for z in range(x):          # word의 조합의 개수
                new += word[y][z]
            text.append(new)            # 발음할 수 있는 단어 추가

    answer = 0
    for i in range(len(babbling)):
        if babbling[i] in text:
            answer += 1
    return answer