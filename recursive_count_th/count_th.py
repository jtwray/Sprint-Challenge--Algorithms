'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    lookfor="th"
    lfLen=len(lookfor)
    if len(word) < lfLen:
        return 0
    if word[0:lfLen]==lookfor:
        return 1 + count_th(word[lfLen-1:])
    return count_th(word[lfLen-1:])