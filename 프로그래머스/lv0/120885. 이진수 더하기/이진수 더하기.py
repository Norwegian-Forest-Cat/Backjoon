def cal(num):
    n = list(num)
    total, index = 0, 0
    for i in range(len(n) - 1, -1, -1):
        total += int(n[i]) * (2 ** index)
        index += 1
    return total

def solution(bin1, bin2):
    a, b = cal(bin1), cal(bin2)
    return str(bin(a + b))[2:]     # 앞의 2자리를 자르기 위해 문자로 변환 -> 파싱 