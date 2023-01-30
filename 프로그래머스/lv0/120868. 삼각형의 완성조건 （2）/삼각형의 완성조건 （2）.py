# 범위 : sides에서 (가장 큰수 - 작은수) ~ (큰수 + 작은수)
def solution(sides):
    sides.sort()
    return (sides[1] + sides[0]) - (sides[1] - sides[0]) - 1