f = open("input.txt", "r")
sum = 0
for x in f:
    x = x.replace("Game ","").replace("\n","")
    x = x.replace(": ", ";")
    x = x.replace("; ",";")
    x = x.split(";")
    ispossible = True
    for i in x[1::]:
        a = i.split(", ")
        for z in a:
            b = z.split(" ")
            if int(b[0])>12 and "red" in b[1]:
                ispossible = False
            elif int(b[0]) > 13 and "green" in b[1]:
                ispossible = False
            elif int(b[0]) > 14 and "blue" in b[1]:
                ispossible = False
    if ispossible:
        sum+=int(x[0])
print(sum)