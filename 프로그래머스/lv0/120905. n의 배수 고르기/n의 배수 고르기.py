def solution(n, numlist):
    for i in range(len(numlist) - 1, -1, -1):   # pop시 index error 방지를 위해 뒤에서부터 탐색한다.
        if numlist[i] % n > 0:
            numlist.pop(i)
    return numlist