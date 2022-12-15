# 세로읽기

arr = [list(input()) for _ in range(5)]
maxN = 0

for i in range(5):      # 한줄에 최대 몇글자인지 확인
    maxN = max(maxN, len(arr[i]))

for i in range(5):      # 비어있을 경우 빈칸 삽입
    while len(arr[i]) < maxN:
        arr[i].append('')

answer = []
for i in range(maxN):      # 순서대로 담는다
    for j in range(5):
        if arr[j][i] != '':
            answer.append(arr[j][i])
print(*answer, sep='')