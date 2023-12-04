f = open("input.txt", "r")
sum = 0
rows = []
for x in f:
    rows.append(x)
def hasspecial(Yindex,Xindex):
    if Yindex==0:
        if rows[Yindex][Xindex-1] == "*" or rows[Yindex][Xindex+1] == "*" or rows[Yindex+1][Xindex-1] == "*" or rows[Yindex+1][Xindex] == "*" or rows[Yindex+1][Xindex+1] == "*":
            return True
    elif Yindex==len(rows)-1:
        if rows[Yindex][Xindex-1] == "*" or rows[Yindex][Xindex+1] == "*" or rows[Yindex-1][Xindex-1] == "*" or rows[Yindex-1][Xindex] == "*" or rows[Yindex-1][Xindex+1] == "*":
            return True
    else:
        if rows[Yindex-1][Xindex-1] == "*" or rows[Yindex-1][Xindex] == "*" or rows[Yindex-1][Xindex+1] == "*" or rows[Yindex][Xindex-1] == "*" or rows[Yindex][Xindex+1] == "*" or rows[Yindex+1][Xindex-1] == "*" or rows[Yindex+1][Xindex] == "*" or rows[Yindex+1][Xindex+1] == "*":
            return True
number = ''
numbers = []
isPart = False
for Yindex,z in enumerate(rows):
    for Xindex,x in enumerate(z):
        if x.isdigit():
            number+=x
            if hasspecial(Yindex,Xindex):
                isPart=True
        else:
            if isPart:
                numbers.append([number, Yindex, Xindex-len(number), Xindex-1])
                isPart = False
            number=''
stars = []
for Yindex,i in enumerate(rows):
    for Xindex, x in enumerate(i):
        if x=='*':
            stars.append([Yindex,Xindex])
twonumbers = []
for i in stars:
    for x in numbers:
        if x[1]>=i[0]-1 and x[1]<=i[0]+1:
            if i[1]>=x[2]-1 and i[1]<=x[3]+1:
                twonumbers.append(int(x[0]))
    if len(twonumbers)==2:
        sum+=twonumbers[0]*twonumbers[1]
    twonumbers=[]
print(sum)