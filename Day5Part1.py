Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line[:-1])

Crates=[]
for i in range(0,int((len(Input[0])+1)/4)):
    Crates.append([])    

for i in range(0,len(Input)):
    if Input[i] == "":
        break
Seperate = i
i+=-1
while i > 0:
    i+=-1
    for j in range(0,int((len(Input[0])+1)/4)):
        if Input[i][(j*4)+1] != " ":
            Crates[j].append(Input[i][(j*4)+1]) 

def MoveCrates(Amount, Target, Destination):
    for i in range(1,Amount+1):
        Destination.append(Target[-i])
    Target = Target[:len(Target)-(Amount)]
    return Target, Destination

for i in range(Seperate+1,len(Input)):
    Line = Input[i].split(" ")
    Crates[int(Line[3])-1], Crates[int(Line[5])-1] = MoveCrates(int(Line[1]),Crates[int(Line[3])-1], Crates[int(Line[5])-1])
    
print(Crates)
