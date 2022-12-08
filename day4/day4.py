def star1():
    with open("input") as f:
        pairs =  f.read().strip().split("\n")
        overlaps = 0
        for p in pairs:
            r1,r2 = p.split(",")
            r1 = r1.split("-")
            r2 = r2.split("-")
            r1 = [int(x) for x in r1]
            r2 = [int(x) for x in r2]
            range1 = set(range(r1[0], r1[1] + 1))
            range2 = set(range(r2[0], r2[1] + 1))

            if range1.issubset(range2) or range2.issubset(range1):
                overlaps += 1

        return overlaps

def star2():
    with open("input") as f:
        pairs =  f.read().strip().split("\n")
        overlaps = 0
        for p in pairs:
            r1,r2 = p.split(",")
            r1 = r1.split("-")
            r2 = r2.split("-")
            r1 = [int(x) for x in r1]
            r2 = [int(x) for x in r2]
            range1 = set(range(r1[0], r1[1] + 1))
            range2 = set(range(r2[0], r2[1] + 1))

            if range1.intersection(range2):
                overlaps += 1

        return overlaps

print(star1())
print(star2())