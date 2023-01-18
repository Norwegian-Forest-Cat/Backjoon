def solution(common):
    if common[1] - common[0] == common[2] - common[1]:  # 등차수열일 경우
        value = common[1] - common[0]
        return common[-1] + value
    else:       # 등비수열인 경우
        value = common[1] // common[0]
        return common[-1] * value