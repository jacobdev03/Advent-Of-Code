food = []
sums = []

with open("input") as f:
    lines = f.readlines()
    for l in lines:
        food.append(l.rstrip())
    food = ' '.join(food).split("  ")

for elf in food:
    sum = 0
    elf = elf.split(' ')
    elf = [int(x) for x in elf]
    for calorie in elf:
        sum += calorie
    sums.append(sum)

sums.sort()

top_three = 0
for e in sums[-3:]:
    top_three += e

print(f"Elf with the most calories: {sums[-1]} ")  
print(f"Top 3 elves sum: {top_three} ")        
