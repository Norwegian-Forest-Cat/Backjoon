# 소수 구하기

import math

a, b = map(int, input().split())

for i in range(a, b+1):
    if i == 1:
        pass
    elif i > 1:
        cnt = 0
        # for j in range(2, int(num**0.5)+1):     <- 아래와 동일
        for j in range(2, int(math.sqrt(i) + 1)):   # 제곱근으로 나눔 + 1 까지만 검사
            if cnt >= 1:
                break
            elif i % j == 0:      # 나누어질 경우 소수가 아님
                cnt += 1
        if cnt == 0:
            print(i)

