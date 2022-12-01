Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)   
elves=[]
temp = 0
for line in Input:
    if line == "\n":
        elves.append(temp)
        temp=0
    else:
        temp = temp + int(line)
elves.sort(reverse=True)
print(elves[0]+elves[1]+elves[2])
