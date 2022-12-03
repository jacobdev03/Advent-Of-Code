import string


values = dict()
for index, letter in enumerate(string.ascii_letters):
    values[letter] = index + 1

with open("input") as f:
    sum = 0
    group = []
    lines = f.readlines()
    for line in lines:
        group.append(line.rstrip())
        for str in line.rstrip().split():
            first_comp = str[:len(str)//2]
            second_comp = str[len(str)//2:]
            same_letter = ''.join(set(first_comp).intersection(second_comp))
            sum += values[same_letter]
    print(sum)


    groups = [group[n:n+3] for n in range(0, len(group), 3)]
    sum2 = 0
    for g in groups:
        rucksack_1 = g[0]
        rucksack_2 = g[1]
        rucksack_3 = g[2]
        badge = ''.join(set(rucksack_1).intersection(rucksack_2).intersection(rucksack_3))
        sum2 += values[badge]
    print(sum2)
        
    


