from __future__ import print_function

verbose = False

f = open('inputs/input02.txt')

total_paper = 0
total_ribbon = 0
for line in f:
    if verbose:
        print("line:", line)
    l, w, d = line.split('x')
    l, w, d = int(l), int(w), int(d)
    if verbose:
        print("Dimensions:", l, w, d)

    # paper
    s1 = l * w
    s2 = l * d
    s3 = w * d
    extra = min(s1, s2, s3)
    paper_needed = 2*s1 + 2*s2 + 2*s3 + extra
    if verbose:
        print("Paper needed for present:", paper_needed)
    total_paper += paper_needed

    # ribbon
    ribbon = min(l+l+w+w, l+l+d+d, w+w+d+d)
    bow = l * w * d
    total_ribbon += (ribbon + bow)

print("Total paper needed:", total_paper)
print("Total ribbin needed:", total_ribbon)
