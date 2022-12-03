Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line[:-1])

Priority = 0
for i in range(0,len(Input),3):
    found=[]
    for item in Input[i]:
        if item in Input[i+1] and item in Input[i+2] and item not in found:
            found.append(item)
            if item == item.upper():
                Priority += ord(item)-38
            else:
                Priority += ord(item)-96
print(Priority)
