def star1():
    with open('input') as f:
        line = f.read()
        for i, _ in enumerate(line):
            if len(set(line[i: i + 4])) == 4:
                return i + 4


def star2():
    with open('input') as f:
        line = f.read()
        for i, _ in enumerate(line):
            if len(set(line[i: i + 14])) == 14:
                return i + 14

print(star1())
print(star2())
