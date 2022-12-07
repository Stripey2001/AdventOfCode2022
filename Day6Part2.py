Input = []
LineReader = open("input.txt","r")
for line in LineReader:
    Input.append(line)
data = Input[0]

markerLen = 14

for i in range(markerLen-1,len(data)):
    unique = True
    check = []
    for m in reversed(range(0,markerLen)):
        check.append(data[i-m])
    for j in range(0,markerLen-1):
        for k in range(j+1,markerLen):
            #print(check[j],check[k])
            if check[j] == check[k]:
                unique = False
    if unique:
        print(i+1)
        break
