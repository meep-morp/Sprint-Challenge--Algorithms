'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) > 1 and word[0] == 't' and word[1] == 'h':
        return 1 + count_th(word[2:])
    elif len(word) > 2:
        return count_th(word[1:])
    else:
        return 0
