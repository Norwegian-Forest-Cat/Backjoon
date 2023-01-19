def solution(cipher, code):
    answer = ''
    N = len(cipher) // code
    for i in range(1, N + 1):
        answer += cipher[i * code - 1]
    return answer