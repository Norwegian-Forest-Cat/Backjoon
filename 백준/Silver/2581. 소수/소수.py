M = int(input())
N = int(input())
bucket = []

for i in range(M, N + 1):
    if i == 1:
        continue
    n = (i ** (1/2)) // 1 + 1
    flag = 0
    for j in range(2, int(n)):
        if i % j == 0:
            flag = 1    # 소수가 아닐경우 flag on
            break
    if flag == 0:
        bucket.append(i)
if len(bucket) == 0:
    print(-1)
else:
    print(sum(bucket))
    print(bucket[0])