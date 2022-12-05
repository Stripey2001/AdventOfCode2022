Input = []
LineReader = open("basic.txt","r")
for line in LineReader:
    Input.append(line)
Crates=[]
for i in range(0,int(len(Input[0])/4)):
    Crates.append([])
Image=True
i=0
while Image:
    if Input[i][1] == "1":
        Image = False
        break
    for j in range(0,int(len(Input[0])/4)):
        Crates[j].append(Input[i][(j*4)+1]) 
    i+=1
print(Crates)
