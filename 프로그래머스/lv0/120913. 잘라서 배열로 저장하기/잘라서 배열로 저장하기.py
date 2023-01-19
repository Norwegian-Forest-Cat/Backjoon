def solution(my_str, n):
    if len(my_str) % n == 0:
        N = len(my_str) // n
    else:
        N = len(my_str) // n + 1

    answer = []
    for i in range(N):
        if i == N - 1:
            answer.append(my_str[i * n:])
        else:
            answer.append(my_str[i * n:i * n + n])
    return answer