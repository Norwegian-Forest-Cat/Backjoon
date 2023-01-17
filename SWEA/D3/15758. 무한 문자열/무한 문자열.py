TC = int(input())
for tc in range(1, TC + 1):
    S, T = input().split()
    N = len(S) + len(T)
    newS, newT = '', ''
    for i in range(N):
        newS += S[i % len(S)]
        newT += T[i % len(T)]

    answer = 'no'
    if newS == newT:
        answer = 'yes'
    print(f'#{tc} {answer}')