'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if word == "":
        return 0

    search_word = "th"

    if word[:2] == search_word:
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])


print(count_th("abcthxyzth"))
