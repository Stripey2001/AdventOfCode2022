Input = []
LineReader = open("basic.txt","r")
for line in LineReader:
    Input.append(line)

Tree = ["/",[]]

for i in range(0,len(Input)):
    if Input[i][0] == "$":
        if Input[i][2:4] == "ls":
            end = False
            print(currentDir)
            while not end:
                i += 1
                if Input[i][0] == "$": 
                    end = True
                else:
                    print(Input[i])
        elif Input[i][2:4] == "cd":
            currentDir = Input[i][5:]
