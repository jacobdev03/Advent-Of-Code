score = 0
rock = 1
paper = 2
scissors = 3
lost = 0
draw = 3
win = 6


# STAR 1


with open("input") as f:
    lines = f.readlines()
    for l in lines:
        choices = l.rstrip().split(" ")
        elf_choice = choices[0]
        my_choice = choices[1]
        if elf_choice == "A" and my_choice == "X":
            score += draw + rock
        elif  elf_choice == "B" and my_choice == "Y":
            score += draw + paper
        elif  elf_choice == "C" and my_choice == "Z":
            score += draw + scissors
        elif  elf_choice == "A" and my_choice == "Y":
            score += win + paper
        elif  elf_choice == "A" and my_choice == "Z":
            score += scissors + lost
        elif  elf_choice == "B" and my_choice == "X":
            score += rock + lost
        elif  elf_choice == "B" and my_choice == "Z":
            score += win + scissors
        elif  elf_choice == "C" and my_choice == "X":
            score += rock + win
        elif  elf_choice == "C" and my_choice == "Y":
            score += lost + paper


# STAR 2
#X means you need to lose
#Y means you need to end the round in a draw
#Z means you need to win.


    score2 = 0
    for l in lines:
        choices = l.rstrip().split(" ")
        elf_choice = choices[0]
        instruction = choices[1]
        if instruction == "X" and elf_choice == "A":
            score2 += lost + scissors            
        elif instruction == "X" and elf_choice == "B":
            score2 += lost + rock
        elif instruction == "X" and elf_choice == "C":
            score2 += lost + paper
        elif instruction == "Y" and elf_choice == "A":
            score2 += draw + rock
        elif instruction == "Y" and elf_choice == "B":
            score2 += draw + paper
        elif instruction == "Y" and elf_choice == "C":
            score2 += draw + scissors
        elif instruction == "Z" and elf_choice == "A":
            score2 += win + paper
        elif instruction == "Z" and elf_choice == "B":
            score2 += win + scissors
        elif instruction == "Z" and elf_choice == "C":
            score2 += win + rock


    print(score)
    print(score2)