Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)
data = Input[0]
    
for i in range(3,len(data)):
    unique = True
    check = [data[i-3],data[i-2],data[i-1],data[i]]
    for j in range(0,3):
        for k in range(j+1,4):
            #print(check[j],check[k])
            if check[j] == check[k]:
                unique = False
    if unique:
        print(i+1)
        break
