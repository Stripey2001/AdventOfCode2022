Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line[:-1])

Priority = 0
i=0
for backpack in Input:
    i+=1
    found=0
    already = []
    comp1 = backpack[:int(len(backpack)/2)]
    comp2 = backpack[int(len(backpack)/2):]
    for item in comp1:
        if item not in already:
            if item in comp2:
                if item == item.upper():
                    Priority += ord(item)-38
                else:
                    Priority += ord(item)-96
        already.append(item)
print(Priority)
