import string


values = dict()
for index, letter in enumerate(string.ascii_letters):
    values[letter] = index + 1

with open("input") as f:
    sum = 0
    lines = f.readlines()
    for line in lines:
        for str in line.rstrip().split():
            first_comp = str[:len(str)//2]
            second_comp = str[len(str)//2:]
            same_letter = ''.join(set(first_comp).intersection(second_comp))
            sum += values[same_letter]
    print(sum)