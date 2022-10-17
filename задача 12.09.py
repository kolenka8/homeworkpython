def find_let(s):
    big = 0
    for letter in s:
        if letter.isupper():
            big += 1
    return True
information = input()
line = information.split()
line_len = len(line)
big_wrd = 0
for find in line:
    if find_let(find): big_wrd += 1
first = big_wrd / line_len * 100
print(' big words: {0} %'.format(first))
