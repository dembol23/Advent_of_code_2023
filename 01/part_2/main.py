f = open("input.txt", "r")
sum=0
for x in f:
    x=x.replace("one","o1e")
    x=x.replace("two","t2o")
    x=x.replace("three","t3e")
    x=x.replace("four","f4r")
    x=x.replace("five","f5e")
    x=x.replace("six","s6x")
    x=x.replace("seven","s7n")
    x=x.replace("eight","e8t")
    x=x.replace("nine","n9e")
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