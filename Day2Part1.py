Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)
Score = 0
for line in Input:
    Op = line[0]
    Me = line[2]
    if Op == "A":
        if Me == "X":
            Score += 1
            Score += 3
        elif Me == "Y":
            Score += 2
            Score += 6
        else:
            Score += 3
            Score += 0
    elif Op == "B":
        if Me == "X":
            Score += 1
            Score += 0
        elif Me == "Y":
            Score += 2
            Score += 3
        else:
            Score += 3
            Score += 6
    else:
        if Me == "X":
            Score += 1
            Score += 6
        elif Me == "Y":
            Score += 2
            Score += 0
        else:
            Score += 3
            Score += 3
print(Score) 
