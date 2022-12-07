# 영화감독 숌
# 규칙을 찾아 알고리즘을 구현하려니 어떻게 정립해야할지 모르겠다
# 다른 풀이를 찾아보니 대부분 완전탐색(Brute Force)로 구현하여 참고하였다.

N = int(input())
movie = 666

while N:    # 영화 순서가 될 경우 while문 off
    if '666' in str(movie):     # 666이 포함된 숫자를 만날경우 횟수 차감
        N -= 1
    movie += 1

print(movie - 1)