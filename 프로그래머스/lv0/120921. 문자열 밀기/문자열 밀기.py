def solution(A, B):
    A, B = list(A), list(B)
    if A == B:
        return 0
    for i in range(len(A)):
        text = A[-1]
        A.pop()
        A.insert(0, text)   # A 앞에 삽입
        print(A)
        if A == B:
            return i + 1
    return -1