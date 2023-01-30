def solution(spell, dic):
    for i in range(len(dic)):
        if len(dic[i]) == len(spell):
            cnt = 0
            for j in range(len(spell)):
                if spell[j] in dic[i]:
                    cnt += 1
            if cnt == len(spell):
                return 1
    return 2