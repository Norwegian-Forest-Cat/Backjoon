# 상수

# 숫자 -> 문자열 변경 후 뒤집기
A, B = map(str, input().split())
A, B = list(A), list(B)
A[0], A[2] = A[2], A[0]
B[0], B[2] = B[2], B[0]

# 문자열 -> 숫자 변경
resultA, resultB = '', ''
for i in range(3):
    resultA += A[i]
    resultB += B[i]
resultA = int(resultA)
resultB = int(resultB)
print(max(resultA, resultB))