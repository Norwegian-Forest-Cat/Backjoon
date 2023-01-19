def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for word in vowel:
        if word in my_string:
            my_string = my_string.replace(word,'')
    return my_string