# 숫자 카드 나누기
# 모든 숫자를 나눌 수 있는 가장 큰수 -> 최대공약수
# 각 배열의 최대공약수 중에 다른 배열을 나눌 수 없는지 검사
# 조건을 만족하는 최대공약수 중 더 큰 값이 정답!

from math import gcd

def cal_gcd(arr):       # 최대공약수 구하기
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd(g, arr[i])      # 각 요소들의 최대공약수를 갱신하며 비교
    return g

def solution(arrayA, arrayB):
    N = len(arrayA)
    gcdA, gcdB = cal_gcd(arrayA), cal_gcd(arrayB)   # A와 B 배열의 최대공약수 구하기

    answer = 0
    cnt1, cnt2 = 0, 0
    for i in range(N):      # 1번 조건 확인
        if arrayB[i] % gcdA != 0:   # B를 나눌 수 있는지 확인
            cnt1 += 1
    if cnt1 == N:        # 모든 수를 나눌 수 없다면
        answer = max(answer, gcdA)      # 조건 만족!


    for i in range(N):      # 2번 조건 확인
        if arrayA[i] % gcdB != 0:  # A를 나눌 수 있는지 확인
            cnt2 += 1
    if cnt2 == N:  # 모든 수를 나눌 수 없다면
        answer = max(answer, gcdB)  # 조건 만족!

    return answer