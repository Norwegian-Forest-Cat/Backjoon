# 아스키코드 이용(소문자 : 97~122번)
def solution(s):
    bucket = [0] * 123  # 0포함이므로 1개 더 만든다.
    for i in range(len(s)):
        bucket[ord(s[i])] += 1

    answer = ''
    for i in range(97, 123):
        if bucket[i] == 1:
            answer += chr(i)    # index 번호를 문자로 변환
    return answer