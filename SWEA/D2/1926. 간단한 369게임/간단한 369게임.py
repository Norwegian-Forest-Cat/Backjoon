N = int(input())
numbers = ['3', '6', '9']
answer = []
for i in range(1, N+1):
    cnt = 0
    for j in range(len(str(i))):    # 각 숫자 자리수마다 numbers가 몇개 들어있는지 확인
        if str(i)[j] in numbers:
            cnt += 1
    if cnt:                         # numbers가 포함되어 있다면 개수만큼 '-' 추가
        answer.append('-' * cnt)
    else:
        answer.append(str(i))
print(*answer)