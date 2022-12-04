Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line[:-1].split(","))

Count = 0
for pair in Input:
    Found=False
    pair[0] = pair[0].split("-")
    pair[1] = pair[1].split("-")
    if int(pair[0][0])<=int(pair[1][1]) and int(pair[0][0])>=int(pair[1][0]):
        Count+=1
        Found=True
    if int(pair[1][0])<=int(pair[0][1]) and int(pair[1][0])>=int(pair[0][0]) and not Found:
        Count+=1
print(Count)
