# 아스키코드 적용 : a = 97 / 0 = 48
# 차이 : 49

def solution(age):
    answer, age = '', str(age)
    for i in range(len(age)):
        answer += chr(ord(age[i]) + 49)
    return answer