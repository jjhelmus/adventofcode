from __future__ import print_function

letters = 'abcdefghijklmnopqrstuvwxyz'
doubles = [c+c for c in letters]
straights = [''.join(t) for t in zip(letters[:-2], letters[1:-1], letters[2:])]
next_letter = {c1: c2 for c1, c2 in zip(letters, letters[1:]+'a')}


def is_valid(s):
    # cannot contain i, o, or l
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    # must include two different pairs of letters
    if sum([d in s for d in doubles]) < 2:
        return False
    # must include a straight of length 3 or greater
    if not any([d in s for d in straights]):
        return False
    return True


def next_password(s):
    s = s[:-1] + next_letter[s[-1]]  # increment the last letter
    for i in range(-1, -8, -1):
        if s[i] == 'a':  # increment n-1 letter is n letter changed to 'a'
            s = s[:i-1] + next_letter[s[i-1]] + s[i:]
        else:
            break
    return s


password = 'hepxcrrq'
while is_valid(password) == False:
    password = next_password(password)
print(password)

password = next_password(password)
while is_valid(password) == False:
    password = next_password(password)
print(password)
