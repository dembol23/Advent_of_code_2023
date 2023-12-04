f = open("input.txt", "r")
sum = 0
for x in f:
    x = x.replace("Game ","").replace("\n","")
    x = x.replace(": ", ";")
    x = x.replace("; ",";")
    x = x.split(";")
    fewestRed = 0
    fewestGreen = 0
    fewestBlue = 0
    for i in x[1::]:
        a = i.split(", ")
        for z in a:
            b = z.split(" ")
            if int(b[0])>fewestRed and "red" in b[1]:
                fewestRed = int(b[0])
            elif int(b[0])>fewestGreen and "green" in b[1]:
                fewestGreen = int(b[0])
            elif int(b[0])>fewestBlue and "blue" in b[1]:
                fewestBlue = int(b[0])
    result = fewestBlue * fewestGreen * fewestRed
    sum += result
print(sum)