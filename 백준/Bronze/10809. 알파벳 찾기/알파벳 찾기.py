# 알파벳 찾기

S = list(input())

bucket = [-1] * 26
for i in range(len(S)):
    if bucket[ord(S[i]) - 97] == -1:
        bucket[ord(S[i]) - 97] = i
print(*bucket)
