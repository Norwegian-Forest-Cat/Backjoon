# 별 찍기 - 2

N = int(input())
space=' '
star = '*'
for i in range(1, N+1):
    print(f'{space * (N-i)}{star * i}')