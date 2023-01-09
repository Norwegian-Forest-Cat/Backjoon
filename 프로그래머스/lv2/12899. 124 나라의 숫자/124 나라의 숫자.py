# 3진법으로 전환 후 0->4, 1->1, 2->2로 치환
# n을 한번 나눌때마다 -1씩 해주면 꼬이지 않는다.

def solution(n):
    number = ['1', '2', '4']
    answer = ''
    while n > 0:
        n -= 1
        answer = number[n % 3] + answer     # 진법 변환은 역순이기 때문에 기존 answer을 뒤에 붙여준다.
        n //= 3
    return answer