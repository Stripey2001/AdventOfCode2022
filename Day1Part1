Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)
max = 0
temp = 0
for line in Input:
    if line == "\n":
        temp = 0
    else:
        temp = temp + int(line)
    if temp > max:
        max = temp
print(max)
