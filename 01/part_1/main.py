f = open("input.txt", "r")
sum=0
for x in f:
    a=0
    for i in x:
        if i.isdigit():
            a=int(i)*10
            break
    for i in x[::-1]:
        if i.isdigit():
            a+=int(i)
            break
    sum+=a
print(sum)