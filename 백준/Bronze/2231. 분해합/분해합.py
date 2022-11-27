# 분해합

N = int(input())
answer = 0
for i in range(N-1, 0, -1):
    data = list(str(i))
    number = i
    for j in range(len(data)):
        number += int(data[j])
    if number == N:
        answer = i
print(answer)